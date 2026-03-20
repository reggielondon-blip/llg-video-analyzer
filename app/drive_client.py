"""
DriveClient — Google Drive API v3 Integration
Uses user OAuth2 credentials (refresh token) so the service can access
ANY file in the firm's Google Drive — no folder sharing required.

Auth env vars required:
    GOOGLE_CLIENT_ID       — OAuth2 client ID from Google Cloud Console
    GOOGLE_CLIENT_SECRET   — OAuth2 client secret
    GOOGLE_REFRESH_TOKEN   — Long-lived refresh token (from scripts/get_token.py)
"""

import os
import io
import json
import logging
from pathlib import Path
from typing import List, Optional, Dict
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

log = logging.getLogger("drive-client")

SCOPES = ["https://www.googleapis.com/auth/drive"]

# Tag added to processed video files so we don't re-analyze them
PROCESSED_PROPERTY_KEY = "llg_analyzed"
PROCESSED_PROPERTY_VALUE = "true"


class DriveClient:

    def __init__(self):
        self.service = self._build_service()

    def _build_service(self):
        """
        Build Drive service using user OAuth2 credentials.
        Automatically refreshes the access token using the stored refresh token.
        """
        client_id     = os.getenv("GOOGLE_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        refresh_token = os.getenv("GOOGLE_REFRESH_TOKEN")

        if not all([client_id, client_secret, refresh_token]):
            raise EnvironmentError(
                "Missing Google OAuth credentials. Set GOOGLE_CLIENT_ID, "
                "GOOGLE_CLIENT_SECRET, and GOOGLE_REFRESH_TOKEN in Railway variables. "
                "Run scripts/get_token.py to generate the refresh token."
            )

        creds = Credentials(
            token=None,                          # will be fetched automatically
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=SCOPES,
        )

        # Force an immediate refresh so we catch credential errors at startup
        creds.refresh(Request())
        log.info("Google Drive authenticated via user OAuth2")
        return build("drive", "v3", credentials=creds, cache_discovery=False)

    # ── File Listing ──────────────────────────────────────────────────────────
    def list_unprocessed_videos(
        self, supported_extensions: set = None, max_results: int = 50
    ) -> List[Dict]:
        """
        List ALL video files across the entire Drive that have not been analyzed.
        Searches by MIME type (catches all video subtypes) and excludes files
        already tagged with PROCESSED_PROPERTY_KEY.
        """
        query = (
            "mimeType contains 'video/' "
            "and trashed = false "
            f"and not properties has {{ key='{PROCESSED_PROPERTY_KEY}' "
            f"and value='{PROCESSED_PROPERTY_VALUE}' }}"
        )

        try:
            results = self.service.files().list(
                q=query,
                fields="files(id, name, mimeType, parents, size, createdTime)",
                pageSize=max_results,
                orderBy="createdTime desc",
                includeItemsFromAllDrives=True,
                supportsAllDrives=True,
                corpora="allDrives"
            ).execute()
            files = results.get("files", [])
            log.info(f"Found {len(files)} unprocessed video(s) across all Drive locations")
            return files
        except Exception as e:
            log.error(f"Failed to list files: {e}", exc_info=True)
            return []

    # ── File Metadata ─────────────────────────────────────────────────────────
    def get_file_metadata(self, file_id: str) -> Dict:
        """Fetch metadata for a single file."""
        try:
            return self.service.files().get(
                fileId=file_id,
                fields="id, name, mimeType, parents, size, createdTime"
            ).execute()
        except Exception as e:
            log.error(f"Failed to get metadata for {file_id}: {e}")
            return {}

    # ── Download ──────────────────────────────────────────────────────────────
    def download_file(self, file_id: str, destination_path: str) -> str:
        """
        Download a Drive file to a local path.
        Handles large files with chunked streaming.
        """
        try:
            request = self.service.files().get_media(fileId=file_id)
            with open(destination_path, "wb") as f:
                downloader = MediaIoBaseDownload(f, request, chunksize=8 * 1024 * 1024)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    if status:
                        log.debug(f"Download progress: {status.progress() * 100:.1f}%")
            size_mb = os.path.getsize(destination_path) / (1024 * 1024)
            log.info(f"Downloaded {size_mb:.1f}MB to {destination_path}")
            return destination_path
        except Exception as e:
            log.error(f"Download failed for {file_id}: {e}", exc_info=True)
            raise

    # ── Upload Summary ────────────────────────────────────────────────────────
    def upload_summary(
        self,
        file_path: str,
        file_name: str,
        parent_folder_id: Optional[str]
    ) -> str:
        """
        Upload the analysis summary .txt file back to the same Drive folder.
        Returns the new file's Drive ID.
        """
        metadata = {
            "name": file_name,
            "mimeType": "text/plain",
            "properties": {"llg_summary": "true"}
        }
        if parent_folder_id:
            metadata["parents"] = [parent_folder_id]

        try:
            media = MediaFileUpload(
                file_path, mimetype="text/plain", resumable=False
            )
            file = self.service.files().create(
                body=metadata, media_body=media, fields="id"
            ).execute()
            file_id = file.get("id")
            log.info(f"Summary uploaded: {file_id}")
            return file_id
        except Exception as e:
            log.error(f"Upload failed: {e}", exc_info=True)
            raise

    # ── Mark as Processed ─────────────────────────────────────────────────────
    def mark_as_processed(self, file_id: str):
        """
        Tag the original video file so it won't be re-analyzed.
        Uses Drive file custom properties.
        """
        try:
            self.service.files().update(
                fileId=file_id,
                body={
                    "properties": {
                        PROCESSED_PROPERTY_KEY: PROCESSED_PROPERTY_VALUE
                    }
                }
            ).execute()
            log.info(f"Marked {file_id} as processed")
        except Exception as e:
            log.warning(f"Could not mark file as processed: {e}")

    # ── Watch Folder ──────────────────────────────────────────────────────────
    def setup_folder_watch(
        self,
        folder_id: str,
        webhook_url: str,
        channel_id: str,
        expiration_hours: int = 168  # 7 days max per Drive API
    ) -> Dict:
        """
        Register a Drive push notification channel on a folder.
        Call this from setup_watch.py to configure webhooks.
        Returns the channel details (save these for renewal).
        """
        import uuid
        import time
        expiration_ms = int((time.time() + expiration_hours * 3600) * 1000)

        body = {
            "id": channel_id or str(uuid.uuid4()),
            "type": "web_hook",
            "address": webhook_url,
            "expiration": expiration_ms,
            "payload": True
        }
        try:
            response = self.service.files().watch(
                fileId=folder_id, body=body
            ).execute()
            log.info(f"Watch channel created: {response}")
            return response
        except Exception as e:
            log.error(f"Failed to set up folder watch: {e}", exc_info=True)
            raise

    def stop_folder_watch(self, channel_id: str, resource_id: str):
        """Stop a Drive watch channel."""
        try:
            self.service.channels().stop(
                body={"id": channel_id, "resourceId": resource_id}
            ).execute()
            log.info(f"Watch channel {channel_id} stopped")
        except Exception as e:
            log.warning(f"Could not stop watch channel: {e}")
