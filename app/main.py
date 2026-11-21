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
from fastapi import FastAPI, BackgroundTasks, Header
from fastapi.responses import JSONResponse

from app.drive_client import DriveClient
from app.video_processor import VideoProcessor
from app.transcriber import Transcriber
from app.analyzer import VideoAnalyzer
from app.email_notifier import EmailNotifier
from app.google_ads_client import GoogleAdsClient
from app.ringcentral_client import RingCentralClient
from app.calendly_client import CalendlyClient
from app.docusign_client import DocuSignClient
from app.integration_gate import auth_status, clamp_int, valid_date

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
google_ads: GoogleAdsClient = None
ringcentral: RingCentralClient = None
calendly: CalendlyClient = None
docusign: DocuSignClient = None

# Serialize jobs: shared Drive client and memory-heavy media processing.
processing_lock = asyncio.Lock()

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
    global google_ads, ringcentral, calendly, docusign
    log.info("Initializing Case Video Analyzer...")
    drive_client = DriveClient()
    transcriber = Transcriber()
    analyzer = VideoAnalyzer()
    notifier = EmailNotifier()
    processor = VideoProcessor()
    google_ads = GoogleAdsClient()
    ringcentral = RingCentralClient()
    calendly = CalendlyClient()
    docusign = DocuSignClient()
    log.info("All clients initialized. Ready.")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "case-video-analyzer",
        "integrations": {
            "google_ads": bool(google_ads and google_ads.enabled),
            "ringcentral": bool(ringcentral and ringcentral.enabled),
            "calendly": bool(calendly and calendly.enabled),
            "docusign": bool(docusign and docusign.enabled),
        },
    }


def _integration_guard(authorization: str | None):
    """Close integration reads until a configured bearer token matches."""
    status = auth_status(authorization)
    if status == "unconfigured":
        return JSONResponse(
            {"detail": "Set INTEGRATIONS_API_TOKEN before reading integration data"},
            status_code=503,
        )
    if status == "unauthorized":
        return JSONResponse({"status": "unauthorized"}, status_code=401)
    return None


@app.get("/ads/report")
async def ads_report(days: int = 30, authorization: str | None = Header(default=None)):
    """Per-campaign Google Ads performance for the trailing `days` window."""
    blocked = _integration_guard(authorization)
    if blocked is not None:
        return blocked
    if not (google_ads and google_ads.enabled):
        return JSONResponse({"status": "disabled", "detail": "GOOGLE_ADS_* env vars not set"})
    days = clamp_int(days, 1, 90)
    rows = await google_ads.get_campaign_performance(days=days)
    return JSONResponse({"status": "ok", "days": days, "campaigns": rows})


@app.get("/calls/log")
async def calls_log(per_page: int = 100, authorization: str | None = Header(default=None)):
    """Recent RingCentral call-log records for the authenticated extension."""
    blocked = _integration_guard(authorization)
    if blocked is not None:
        return blocked
    if not (ringcentral and ringcentral.enabled):
        return JSONResponse({"status": "disabled", "detail": "RINGCENTRAL_* env vars not set"})
    per_page = clamp_int(per_page, 1, 100)
    records = await ringcentral.get_call_log(per_page=per_page)
    return JSONResponse({"status": "ok", "count": len(records), "records": records})


@app.get("/calendly/events")
async def calendly_events(count: int = 20, authorization: str | None = Header(default=None)):
    """Upcoming Calendly consultations for the token owner."""
    blocked = _integration_guard(authorization)
    if blocked is not None:
        return blocked
    if not (calendly and calendly.enabled):
        return JSONResponse({"status": "disabled", "detail": "CALENDLY_API_TOKEN not set"})
    count = clamp_int(count, 1, 100)
    events = await calendly.list_scheduled_events(count=count)
    return JSONResponse({"status": "ok", "count": len(events), "events": events})


@app.get("/docs/envelopes")
async def docs_envelopes(
    from_date: str = "2024-01-01",
    authorization: str | None = Header(default=None),
):
    """DocuSign envelopes (with status) created since from_date (YYYY-MM-DD)."""
    blocked = _integration_guard(authorization)
    if blocked is not None:
        return blocked
    if not (docusign and docusign.enabled):
        return JSONResponse({"status": "disabled", "detail": "DOCUSIGN_* env vars not set"})
    if not valid_date(from_date):
        return JSONResponse(
            {"status": "error", "detail": "from_date must be YYYY-MM-DD"},
            status_code=400,
        )
    envelopes = await docusign.list_envelopes(from_date=from_date)
    return JSONResponse({"status": "ok", "count": len(envelopes), "envelopes": envelopes})


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
        async with processing_lock:
            files = await asyncio.to_thread(drive_client.list_unprocessed_videos)
        log.info(f"Found {len(files)} unprocessed video(s) (triggered by: {source})")
        for f in files:
            await process_video_file(f["id"])
    except Exception as e:
        log.error(f"Error scanning Drive: {e}", exc_info=True)


async def process_video_file(file_id: str):
    async with processing_lock:
        await _process_video_file(file_id)


async def _process_video_file(file_id: str):
    tmp_dir = None
    try:
        # ── 1. Get file metadata ──────────────────────────────────────────
        meta = await asyncio.to_thread(drive_client.get_file_info, file_id)
        file_name = meta.get("name", file_id)
        mime_type = meta.get("mimeType", "")
        parents = meta.get("parents", [])
        folder_id = parents[0] if parents else None

        log.info(f"Processing: {file_name} ({mime_type})")

        ext = Path(file_name).suffix.lower()
        if mime_type not in SUPPORTED_VIDEO_TYPES and ext not in SUPPORTED_EXTENSIONS:
            log.info(f"Skipping non-video file: {file_name}")
            return

        if meta.get("appProperties", {}).get("llg_analyzed") == "true":
            log.info("Skipping already processed video: %s", file_id)
            return

        # ── 2. Download video ─────────────────────────────────────────────
        tmp_dir = tempfile.mkdtemp(prefix="llg_video_")
        video_path = os.path.join(tmp_dir, "source" + ext)
        log.info(f"Downloading to {video_path}...")
        await asyncio.to_thread(drive_client.download_file, file_id, video_path)

        # ── 3. Extract audio + frames ─────────────────────────────────────
        log.info("Extracting audio and key frames...")
        audio_path, frame_paths, duration_seconds = await asyncio.to_thread(
            processor.extract, video_path, tmp_dir
        )
        log.info(f"Duration: {duration_seconds:.0f}s | Frames: {len(frame_paths)}")

        # ── 4. Transcribe ─────────────────────────────────────────────────
        transcript = ""
        if audio_path and os.path.exists(audio_path):
            log.info("Transcribing audio with AssemblyAI...")
            transcript = await transcriber.transcribe(audio_path)
            log.info(f"Transcript length: {len(transcript)} chars")
        else:
            log.info("Video has no audio stream — visual-only analysis")

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
        view_link = await asyncio.to_thread(drive_client.upload_analysis, analysis, file_id, file_name)
        log.info(f"Analysis saved: {view_link}")

        # Save successful state before optional notification, avoiding duplicate reports
        # when a notification fails. Upstream failures never reach this point.
        await asyncio.to_thread(drive_client.mark_as_processed, file_id)

        # — 6b. Notify via email —
        await notifier.post_analysis_complete(
            file_name=file_name,
            summary=analysis,
            drive_link=view_link,
            duration_seconds=duration_seconds,
            transcript_chars=len(transcript),
        )

        # ── 7. Mark as processed ──────────────────────────────────────────
        log.info(f"Pipeline complete for: {file_name}")

    except Exception as e:
        log.error(f"Pipeline error for file {file_id}: {e}", exc_info=True)
        await notifier.post_error(file_id, str(e))
    finally:
        if tmp_dir and os.path.exists(tmp_dir):
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)
