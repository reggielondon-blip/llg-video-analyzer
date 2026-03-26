"""
L & L Law Group — Case Video Analyzer
Railway FastAPI Service
Handles Google Drive webhooks, processes body cam / in-car video,
transcribes audio, analyzes with Claude, and saves analysis to Drive.
"""

import os
import logging
import tempfile
import asyncio
from pathlib import Path
from fastapi import FastAPI, BackgroundTasks
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

drive_client: DriveClient = None
transcriber: Transcriber = None
analyzer: VideoAnalyzer = None
notifier: EmailNotifier = None
processor: VideoProcessor = None

SUPPORTED_VIDEO_TYPES = {
    "video/mp4", "video/quicktime", "video/x-msvideo",
    "video/x-matroska", "video/webm", "video/mpeg",
    "video/x-ms-wmv", "video/3gpp", "video/m4v"
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


@app.post("/analyze/file/{file_id}")
async def analyze_file(file_id: str, background_tasks: BackgroundTasks):
    log.info(f"Received request to analyze file: {file_id}")
    background_tasks.add_task(process_video_file, file_id)
    return JSONResponse({"status": "queued", "file_id": file_id})


@app.post("/analyze/folder")
async def analyze_folder(background_tasks: BackgroundTasks):
    background_tasks.add_task(scan_and_process_new_videos, "manual")
    return JSONResponse({"status": "scan_queued"})


async def scan_and_process_new_videos(source: str = "manual"):
    try:
        files = drive_client.list_unprocessed_videos()
        log.info(f"Found {len(files)} unprocessed video(s) (triggered by: {source})")
        for f in files:
            await process_video_file(f["id"])
    except Exception as e:
        log.error(f"Error scanning Drive: {e}", exc_info=True)


async def process_video_file(file_id: str):
    tmp_dir = None
    try:
        # ── 1. Get file metadata ──────────────────────────────────────────
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

        # ── 2. Download video ─────────────────────────────────────────────
        tmp_dir = tempfile.mkdtemp(prefix="llg_video_")
        video_path = os.path.join(tmp_dir, file_name)
        log.info(f"Downloading to {video_path}...")
        drive_client.download_file(file_id, video_path)

        # ── 3. Extract audio + frames ─────────────────────────────────────
        log.info("Extracting audio and key frames...")
        audio_path, frame_paths, duration_seconds = processor.extract(
            video_path, tmp_dir
        )
        log.info(f"Duration: {duration_seconds:.0f}s | Frames: {len(frame_paths)}")

        # ── 4. Transcribe ─────────────────────────────────────────────────
        transcript = ""
        if audio_path and os.path.exists(audio_path):
            log.info("Transcribing audio with AssemblyAI...")
            transcript = await transcriber.transcribe(audio_path)
            log.info(f"Transcript length: {len(transcript)} chars")
        else:
            log.warning("No audio extracted — skipping transcription")

        # ── 5. Analyze with Claude ────────────────────────────────────────
        log.info("Sending to Claude for legal analysis...")
        analysis = await analyzer.analyze(
            file_name=file_name,
            transcript=transcript,
            frame_paths=frame_paths,
            duration_seconds=duration_seconds,
        )
        log.info("Analysis complete")

        # ── 6. Save analysis to Drive ─────────────────────────────────────
        log.info("Saving analysis to Drive...")
        view_link = drive_client.upload_analysis(analysis, file_id, file_name)
        log.info(f"Analysis saved: {view_link}")

        # ── 7. Mark as processed ──────────────────────────────────────────
        drive_client.mark_as_processed(file_id)
        log.info(f"Pipeline complete for: {file_name}")

    except Exception as e:
        log.error(f"Pipeline error for file {file_id}: {e}", exc_info=True)
    finally:
        if tmp_dir and os.path.exists(tmp_dir):
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)
