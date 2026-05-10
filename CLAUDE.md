# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this is

A FastAPI service that analyzes police body-cam / dashcam video for L & L Law Group. It watches a Google Drive folder, downloads new videos, extracts audio + key frames with FFmpeg, transcribes with AssemblyAI (speaker diarization), runs a defense-focused 10-section legal analysis through the Claude API, then writes the result back to Drive as `<filename>_ANALYSIS.txt`.

Deployed on Railway from the `Dockerfile` (Python 3.11 + FFmpeg). Entry point: `uvicorn app.main:app`.

## Layout

```
app/
  main.py              FastAPI app, startup, pipeline orchestration
  drive_client.py      Google Drive v3 client (Service Account auth)
  video_processor.py   FFmpeg wrapper: audio + frame extraction
  transcriber.py       AssemblyAI transcription with speaker diarization
  analyzer.py          Claude API call + the legal analysis prompt
  email_notifier.py    Gmail SMTP notifier (see "Known inconsistencies")
scripts/
  setup_watch.py       Registers a Drive push-notification channel (see notes)
  get_token.py         OAuth2 refresh-token flow (alternative to Service Account; see notes)
Dockerfile             python:3.11-slim + ffmpeg
railway.toml           Railway build/deploy config (uses Dockerfile, /health probe)
requirements.txt       Pinned deps (fastapi, uvicorn, aiohttp, google-api-*, etc.)
README.md              End-user setup guide (Railway, Drive, Slack, Zapier)
```

## Pipeline (app/main.py: `process_video_file`)

1. `DriveClient.get_file_info(file_id)` — fetch metadata, parents, mime
2. Skip if neither MIME nor extension is in the supported sets
3. `DriveClient.download_file` → `tempfile.mkdtemp(prefix="llg_video_")`
4. `VideoProcessor.extract` → `(audio_path, frame_paths, duration_seconds)`
5. `Transcriber.transcribe(audio_path)` → text with `[MM:SS] SPEAKER N:` lines
6. `VideoAnalyzer.analyze(...)` → multimodal Claude call (frames + transcript)
7. `DriveClient.upload_analysis` → writes `<name>_ANALYSIS.txt` next to the source
8. `DriveClient.mark_as_processed` → sets `appProperties.llg_analyzed=true`
9. `tempfile` cleanup in `finally`

`scan_and_process_new_videos` lists everything missing the `llg_analyzed` appProperty across all drives and reprocesses them.

## HTTP endpoints (only what actually exists)

| Method | Path                    | Purpose                              |
| ------ | ----------------------- | ------------------------------------ |
| GET    | `/health`               | Liveness probe (used by Railway)     |
| POST   | `/analyze/file/{id}`    | Queue one file for processing        |
| POST   | `/analyze/folder`       | Queue a full Drive scan              |

Both POSTs use `BackgroundTasks` and return immediately (`{"status": "queued"}`). There is no synchronous response with results.

## Environment variables

Required for the service to do real work:

- `ANTHROPIC_API_KEY` — analyzer; absence yields `[Analysis skipped — ...]`
- `ASSEMBLYAI_API_KEY` — transcriber; absence yields `[Transcription skipped — ...]`
- `GOOGLE_SERVICE_ACCOUNT_JSON` — full JSON of the service-account key, pasted as one variable. `DriveClient.__init__` raises `EnvironmentError` if missing.

Optional:

- `NOTIFY_EMAIL_FROM`, `NOTIFY_EMAIL_PASSWORD`, `NOTIFY_EMAIL_TO` — Gmail SMTP notifier (uses `smtp.gmail.com:465`, app password not account password)
- `DRIVE_WATCH_FOLDER_ID`, `WEBHOOK_BASE_URL` / `RAILWAY_PUBLIC_URL` — only used by `scripts/setup_watch.py`

There is no `.env.example` file in the repo despite the README referring to one; treat the README's variable table as the source of truth for ops, and this file for code-level facts.

## Conventions to follow when changing code

- **Async I/O.** External calls (`aiohttp`, `aiofiles`) are async; FFmpeg/`subprocess` calls are sync and run inside async handlers — keep them under their existing timeouts (`audio: 600s`, `frames: 300s`, `ffprobe: 30s`). The Claude call has a `300s` total timeout; AssemblyAI polling caps at `TIMEOUT = 1800s`.
- **Logging.** Use module-level `log = logging.getLogger("<name>")` (see existing names: `case-video-analyzer`, `drive-client`, `video-processor`, `transcriber`, `analyzer`, `email-notifier`). The root logger is configured once in `main.py`.
- **Tempfiles.** All per-job artifacts live in `tempfile.mkdtemp(prefix="llg_video_")`; the `finally` block in `process_video_file` is responsible for removing it. Don't write into `/app` or `cwd`.
- **Drive API.** Every Drive call must pass `supportsAllDrives=True`; list calls also need `includeItemsFromAllDrives=True` and `corpora="allDrives"`. The "already processed" gate is the `appProperties.llg_analyzed=true` flag — preserve this. Constants: `PROCESSED_PROPERTY_KEY`, `PROCESSED_PROPERTY_VALUE`.
- **Supported video types.** Two parallel sets in `app/main.py` (`SUPPORTED_VIDEO_TYPES` MIME, `SUPPORTED_EXTENSIONS`) and one in `app/drive_client.py` (`SUPPORTED_MIME_TYPES`). Update all three together when adding a format.
- **Frame & audio settings.** `VideoProcessor.FRAME_INTERVAL=10s`, `MAX_FRAMES=20`, `AUDIO_SAMPLE_RATE=16000`. `VideoAnalyzer.MAX_FRAMES_TO_CLAUDE=12` caps how many of those 20 are forwarded. The audio filter `highpass=80,lowpass=8000` is intentional for body-cam wind/vehicle noise — don't widen it without a reason.
- **Transcription quality.** `speaker_labels=True`, `speakers_expected=3` (officer/subject/bystander), `filter_profanity=False` (evidence integrity), `language_detection=True` (Spanish-speaking clients). The `word_boost` list is law-enforcement specific; add to it rather than replacing.
- **Legal prompt.** `analyzer.SYSTEM_PROMPT` and `build_analysis_prompt` define a 10-section defense-perspective output. Treat this as a contract — the email preview parser (`email_notifier._extract_preview`) and the Drive output filename suffix `_ANALYSIS.txt` depend on it. Don't reorder sections without updating both.
- **Claude API.** Calls go directly via `aiohttp` to `https://api.anthropic.com/v1/messages` with header `anthropic-version: 2023-06-01`. Multimodal payload structure is hand-rolled (`{"type":"image","source":{"type":"base64",...}}`). The model is pinned in `analyzer.CLAUDE_MODEL` — see "Known inconsistencies" before changing it.

## Local development

There is no test suite, no linter config, and no CI. The expected loop is:

```bash
pip install -r requirements.txt
# Set the env vars above (a local .env file is read by scripts/setup_watch.py only)
uvicorn app.main:app --reload --port 8080
# In another terminal:
curl -X POST http://localhost:8080/analyze/folder
# or
curl -X POST http://localhost:8080/analyze/file/<drive-file-id>
```

FFmpeg + ffprobe must be on `PATH` locally (the Dockerfile installs them on Railway).

## Deployment

`railway.toml` builds the `Dockerfile` and runs `uvicorn app.main:app --host 0.0.0.0 --port 8080`, with a `/health` probe and `ON_FAILURE` restarts (max 3). Pushing to the configured branch triggers Railway's auto-deploy. Set env vars in the Railway Variables tab.

## Known inconsistencies (read before "fixing")

These look like bugs but reflect a half-finished migration. Confirm with the user before "cleaning them up" — they may be wired up by external tooling (Zapier, manual cron) the repo doesn't show.

1. **Notifier is initialized but never invoked.** `main.py` imports and instantiates `EmailNotifier` at startup, but `process_video_file` never calls `notifier.post_analysis_complete(...)` or `notifier.post_error(...)`. The README still describes Slack notifications, while the only notifier in code is Gmail SMTP. If asked to "fix notifications," clarify which channel (Slack vs. email) is wanted.
2. **`/webhook/drive` is referenced but not implemented.** `scripts/setup_watch.py` and the README both point at `/webhook/drive`, but `app/main.py` has no such route. Drive push channels won't work until that endpoint exists.
3. **`setup_watch.py` calls a method that doesn't exist.** It invokes `DriveClient.setup_folder_watch(...)` and `setup_watch_renew` paths, but `DriveClient` defines no `setup_folder_watch`. The script will raise `AttributeError` as-is.
4. **Two auth strategies live side by side.** `drive_client.py` uses a Service Account (`GOOGLE_SERVICE_ACCOUNT_JSON`). `scripts/get_token.py` produces a `GOOGLE_REFRESH_TOKEN` for an OAuth user flow and even tells the user to delete the service-account vars. Only the Service Account path is wired into the running service.
5. **Model pin is stale.** `analyzer.CLAUDE_MODEL = "claude-opus-4-5"`. The current Anthropic Opus is `claude-opus-4-7`; bumping it is a one-line change but should be coordinated with whoever owns billing/output expectations.

## Git workflow

When this guidance was written the working branch was `claude/add-claude-documentation-4XR62`. Follow whatever branch the user names; don't push to `main` without explicit instruction. Don't create PRs unless asked.
