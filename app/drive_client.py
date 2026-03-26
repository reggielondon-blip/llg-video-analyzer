"""
DriveClient — Google Drive API v3 Integration
Uses Service Account credentials — never expires, no token refresh needed.

To grant access to all of Drive:
  1. Copy the client_email from your service account JSON
  2. Go to drive.google.com
  3. Right-click "My Drive" (the root) → Share
  4. Paste the service account email → Editor → Share
  This gives the service account access to every file in your Drive.

Required env var:
    GOOGLE_SERVICE_ACCOUNT_JSON  — full contents of the downloaded JSON key file
"""

import os
import io
import json
import logging
from typing import List, Dict, Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

log = logging.getLogger("drive-client")

SCOPES = ["https://www.googleapis.com/auth/drive"]
PROCESSED_PROPERTY_KEY   = "llg_analyzed"
PROCESSED_PROPERTY_VALUE = "true"

SUPPORTED_MIME_TYPES = [
    "video/mp4", "video/quicktime", "video/x-msvideo",
    "video/x-matroska", "video/webm", "video/mpeg",
    "video/x-ms-wmv", "video/3gpp", "video/m4v",
]


class DriveClient:

    def __init__(self):
        self.service = self._build_service()

    def _build_service(self):
        creds_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
        if not creds_json:
            raise EnvironmentError(
                "GOOGLE_SERVICE_ACCOUNT_JSON is not set. "
                "Paste the full contents of your service account JSON key into Railway Variables."
            )
        creds_dict = json.loads(creds_json)
        creds = service_account.Credentials.from_service_account_info(
            creds_dict, scopes=SCOPES
        )
        log.info(f"Google Drive authenticated via service account: {creds_dict.get('client_email')}")
        return build("drive", "v3", credentials=creds, cache_discovery=False)

    # ── List all unprocessed videos across entire Drive ───────────────────────
    def list_unprocessed_videos(self) -> List[Dict]:
        """
        Search ALL of Drive for video files that haven't been analyzed yet.
        Excludes files already tagged with llg_analyzed=true.
        """
        mime_filter = " or ".join(
            [f"mimeType='{m}'" for m in SUPPORTED_MIME_TYPES]
        )
        query = (
            f"({mime_filter})"
            f" and not appProperties has {{ key='{PROCESSED_PROPERTY_KEY}'"
            f" and value='{PROCESSED_PROPERTY_VALUE}' }}"
            f" and trashed=false"
        )

        videos = []
        page_token = None

        while True:
            resp = self.service.files().list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, size, createdTime, parents)",
                pageSize=50,
                pageToken=page_token,
            ).execute()

            videos.extend(resp.get("files", []))
            page_token = resp.get("nextPageToken")
            if not page_token:
                break

        log.info(f"Found {len(videos)} unprocessed video(s) across all of Drive")
        return videos

    # ── Download a file ───────────────────────────────────────────────────────
    def download_file(self, file_id: str, dest_path: str) -> str:
        request = self.service.files().get_media(fileId=file_id)
        with open(dest_path, "wb") as f:
            downloader = MediaIoBaseDownload(f, request, chunksize=10 * 1024 * 1024)
            done = False
            while not done:
                _, done = downloader.next_chunk()
        log.info(f"Downloaded file {file_id} → {dest_path}")
        return dest_path

    # ── Upload analysis result back to Drive ─────────────────────────────────
    def upload_analysis(self, content: str, original_file_id: str, original_name: str) -> str:
        """Upload the analysis .txt file to the same folder as the original video."""
        # Get the parent folder of the original video
        file_meta = self.service.files().get(
            fileId=original_file_id, fields="parents"
        ).execute()
        parents = file_meta.get("parents", [])

        analysis_name = original_name.rsplit(".", 1)[0] + "_ANALYSIS.txt"
        media = MediaFileUpload(
            io.BytesIO(content.encode("utf-8")),
            mimetype="text/plain",
            resumable=False,
        )

        # MediaFileUpload doesn't accept BytesIO directly — write to temp file
        import tempfile, os
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            file_metadata = {"name": analysis_name, "parents": parents}
            uploaded = self.service.files().create(
                body=file_metadata,
                media_body=MediaFileUpload(tmp_path, mimetype="text/plain"),
                fields="id, webViewLink",
            ).execute()
            log.info(f"Uploaded analysis: {analysis_name} → {uploaded.get('webViewLink')}")
            return uploaded.get("webViewLink", "")
        finally:
            os.unlink(tmp_path)

    # ── Mark a video as processed ─────────────────────────────────────────────
    def mark_as_processed(self, file_id: str):
        self.service.files().update(
            fileId=file_id,
            body={"appProperties": {PROCESSED_PROPERTY_KEY: PROCESSED_PROPERTY_VALUE}},
        ).execute()
        log.info(f"Marked {file_id} as processed")

    # ── Get file metadata ─────────────────────────────────────────────────────
    def get_file_info(self, file_id: str) -> Dict:
        return self.service.files().get(
            fileId=file_id,
            fields="id, name, mimeType, size, createdTime, webViewLink"
        ).execute()
def get_file_metadata(self, file_id: str) -> dict:
        return self.get_file_info(file_id)
