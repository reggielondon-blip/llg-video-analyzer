"""
L & L Law Group — Case Video Analyzer
Railway FastAPI Service
Handles Google Drive webhooks, processes body cam / in-car video,
transcribes audio, analyzes with Claude, and sends an email summary.
"""

import os
import logging
import tempfile
import asyncio
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from app.drive_client import DriveClient
from app.video_processor import VideoProcessor
from app.transcriber import Transcriber
from app.analyzer import VideoAnalyzer
from app.email_notifier import EmailNotifier

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
log = logging.getLogger("case-video-analyzer")

app = FastAPI(
    title="L&L Case Video Analyzer",
    description="Body cam and in-car video analysis for L & L Law Group",
    version="1.0.0"
)

# ── Clients (initialized at startup) ────────────────────────────────────────
drive_client: DriveClient = None
transcriber: Transcriber = None
analyzer: VideoAnalyzer = None
notifier: EmailNotifier = None
processor: VideoProcessor = None

SUPPORTED_VIDEO_TYPES = {
    "video/mp4", "video/quicktime", "video/x-msvideo",
    "video/x-matroska", "video/webm", "video/mpeg",
    "video/x-ms-wmv", "video/3gpp"
}

SUPPORTED_EXTENSIONS = {
    ".mp4", ".mov", ".avi", ".mkv", ".webm",
    ".mpg", ".mpeg", ".wmv", ".3gp", ".m4v"
}


@app.on_event("startup")
async def startup():
    global drive_client, transcriber, analyzer, notifier, processor
    log.info("Initializing Case Video Analyzer...")
    drive_client = DriveClient()
    transcriber = Transcriber()
    analyzer = VideoAnalyzer()
    notifier = EmailNotifier()
    processor = VideoProcessor()
    log.info("All clients initialized. Ready.")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "case-video-analyzer"}


# ── Google Drive Push Webhook ────────────────────────────────────────────────
@app.post("/webhook/drive")
async def drive_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Receives Google Drive push notifications when files are added/changed
    in the watched folder. Enqueues video files for processing.
    """
    headers = dict(request.headers)

    # Drive sends a resource state header
    resource_state = headers.get("x-goog-resource-state", "")
    channel_id = headers.get("x-goog-channel-id", "")
    resource_id = headers.get("x-goog-resource-id", "")

    log.info(f"Drive webhook received: state={resource_state} channel={channel_id}")

    # 'sync' is the initial handshake — acknowledge and ignore
    if resource_state == "sync":
        return JSONResponse({"status": "sync_acknowledged"})

    # Only process 'add' or 'update' events
    if resource_state not in ("add", "update", "change"):
        return JSONResponse({"status": "ignored", "state": resource_state})

    background_tasks.add_task(scan_and_process_new_videos, channel_id)

    return JSONResponse({"status": "queued"})


# ── Manual Trigger (for testing or Zapier) ──────────────────────────────────
@app.post("/analyze/file/{file_id}")
async def analyze_file_by_id(file_id: str, background_tasks: BackgroundTasks):
    """
    Manually trigger analysis of a specific Drive file by ID.
    Useful for Zapier triggers or manual testing.
    """
    background_tasks.add_task(process_video_file, file_id)
    return JSONResponse({"status": "queued", "file_id": file_id})


@app.post("/analyze/folder")
async def analyze_folder(background_tasks: BackgroundTasks):
    """
    Manually scan ALL of Google Drive for unprocessed videos.
    """
    background_tasks.add_task(scan_and_process_new_videos, "manual")
    return JSONResponse({"status": "scan_queued", "scope": "all_drive"})


# ── Core Processing Pipeline ─────────────────────────────────────────────────
async def scan_and_process_new_videos(source: str = "manual"):
    """
    Scans ALL of Google Drive for unprocessed video files and processes each.
    """
    try:
        files = drive_client.list_unprocessed_videos()
        log.info(f"Found {len(files)} unprocessed video(s) across all Drive locations (triggered by: {source})")
        for f in files:
            await process_video_file(f["id"])
    except Exception as e:
        log.error(f"Error scanning Drive: {e}", exc_info=True)


async def process_video_file(file_id: str):
    """
    Full pipeline for a single video file:
    1. Download from Drive
    2. Extract audio + key frames
    3. Transcribe audio
    4. Analyze with Claude
    5. Save summary to Drive
    6. Email summary
    """
    tmp_dir = None
        try:
            # — 1. Get file metadata ————————————————
            meta = drive_client.get_file_info(file_id)
            file_name = meta.get("name", file_id)
        mime_type = meta.get("mimeType", "")
        parents = meta.get("parents", [])
        folder_id = parents[0] if parents else None

        log.info(f"Processing: {file_name} ({mime_type})")

        ext = Path(file_name).suffix.lower()
        if mime_type not in SUPPORTED_VIDEO_TYPES and ext not in SUPPORTED_EXTENSIONS:
            log.info(f"Skipping non-video file: {file_name}")
            return

        # ── 2. Download video ───────────────────────────────────────────
        tmp_dir = tempfile.mkdtemp(prefix="llg_video_")
        video_path = os.path.join(tmp_dir, file_name)
        log.info(f"Downloading to {video_path}...")
        drive_client.download_file(file_id, video_path)

        # ── 3. Extract audio + frames ───────────────────────────────────
        log.info("Extracting audio and key frames...")
        audio_path, frame_paths, duration_seconds = processor.extract(
            video_path, tmp_dir
        )
        log.info(f"Duration: {duration_seconds:.0f}s | Frames: {len(frame_paths)}")

        # ── 4. Transcribe ───────────────────────────────────────────────
        transcript = ""
        if audio_path and os.path.exists(audio_path):
            log.info("Transcribing audio...")
            transcript = await transcriber.transcribe(audio_path)
            log.info(f"Transcript length: {len(transcript)} chars")
        else:
            log.warning("No audio extracted; skipping transcription")

        # ── 5. Analyze with Claude ──────────────────────────────────────
        log.info("Sending to Claude for analysis...")
        summary = await analyzer.analyze(
            file_name=file_name,
            transcript=transcript,
            frame_paths=frame_paths,
            duration_seconds=duration_seconds
        )

        # ── 6. Save summary to Drive ────────────────────────────────────
        summary_filename = Path(file_name).stem + "_ANALYSIS.txt"
        summary_path = os.path.join(tmp_dir, summary_filename)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        drive_file_id = drive_client.upload_summary(
            summary_path, summary_filename, folder_id
        )
        drive_link = f"https://drive.google.com/file/d/{drive_file_id}/view"
        log.info(f"Summary saved to Drive: {drive_link}")

        # Mark original as processed
        drive_client.mark_as_processed(file_id)

        # ── 7. Email summary ────────────────────────────────────────────
        await notifier.post_analysis_complete(
            file_name=file_name,
            summary=summary,
            drive_link=drive_link,
            duration_seconds=duration_seconds,
            transcript_chars=len(transcript)
        )

        log.info(f"✓ Done: {file_name}")

    except Exception as e:
        log.error(f"Pipeline error for file {file_id}: {e}", exc_info=True)
        try:
            await notifier.post_error(file_id=file_id, error=str(e))
        except Exception:
            pass
    finally:
        # Clean up temp files
        if tmp_dir and os.path.exists(tmp_dir):
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)
