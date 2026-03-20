# llg-video-analyzer
# L & L Law Group — Case Video Analyzer

AI-powered analysis of body cam and in-car (dashcam) video evidence.
Watches a Google Drive folder, auto-processes new videos, and posts
a complete defense-focused legal analysis to Slack.

---

## What It Does

1. **Watches** a Google Drive folder for new video files (.mp4, .mov, .avi, etc.)
2. **Extracts** audio and key frames using FFmpeg
3. **Transcribes** audio with AssemblyAI (speaker diarization — separates officer vs. subject)
4. **Analyzes** with Claude (10-section legal analysis: stop, search, Miranda, defense observations, suppression flags)
5. **Saves** the full analysis as a `.txt` file in the same Drive folder
6. **Notifies** Slack with a summary and link to the full analysis

---

## Setup: Step by Step

### Prerequisites
- Railway account with a service (you already have this)
- GitHub account (you already have this)
- AssemblyAI account — free tier works for testing
- Google Cloud project with Drive API enabled

---

### Step 1: Get an AssemblyAI API Key

1. Go to [assemblyai.com](https://www.assemblyai.com) → Sign up (free)
2. Dashboard → API Keys → copy your key
3. Cost: ~$0.37/hour of audio. A 30-min body cam video = ~$0.19.

---

### Step 2: Create a Google Service Account

This is how the service authenticates to Google Drive.

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Select your project (or create one: "LLG Video Analyzer")
3. APIs & Services → Enable APIs → enable **Google Drive API**
4. APIs & Services → Credentials → **Create Credentials** → Service Account
   - Name: `llg-video-analyzer`
   - Role: `Editor` (or `Drive API - File Metadata Writer`)
5. Click the service account → **Keys** → Add Key → JSON → Download
6. Open the downloaded JSON file — you'll paste its entire contents as an env var

#### Share the Drive Folder with the Service Account
1. Create a folder in Google Drive: **"Evidence Videos"** (or your preferred name)
2. Right-click → Share → paste the service account email
   - It looks like: `llg-video-analyzer@your-project.iam.gserviceaccount.com`
3. Give it **Editor** access
4. Copy the folder ID from the URL:
   `https://drive.google.com/drive/folders/THIS_IS_YOUR_FOLDER_ID`

---

### Step 3: Create a Slack Incoming Webhook

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create App → From scratch
   - App Name: `Case Video Analyzer`
   - Workspace: L & L Law Group
2. Features → Incoming Webhooks → toggle ON
3. Add New Webhook → select `#customerservice` channel → Allow
4. Copy the webhook URL: `https://hooks.slack.com/services/...`

---

### Step 4: Deploy to Railway

1. Push this project to a GitHub repo
2. Railway Dashboard → New Project → Deploy from GitHub → select repo
3. **Variables** tab → add all variables from `.env.example`:

| Variable | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `ASSEMBLYAI_API_KEY` | From Step 1 |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Entire JSON from Step 2 (paste as-is) |
| `DRIVE_WATCH_FOLDER_ID` | Folder ID from Step 2 |
| `SLACK_WEBHOOK_URL` | From Step 3 |
| `SLACK_CHANNEL` | `#customerservice` |

4. Railway will build and deploy automatically (uses Dockerfile with FFmpeg)
5. Note your Railway public URL: `https://your-service.up.railway.app`

---

### Step 5: Register the Drive Folder Watch

This tells Google Drive to notify your Railway service when files are added.

**Option A: Run the setup script**
```bash
# Set your env vars locally, then:
WEBHOOK_BASE_URL=https://your-service.up.railway.app python scripts/setup_watch.py
```

**Option B: Manual API call**
```bash
curl -X POST https://your-service.up.railway.app/analyze/folder
```
This triggers a manual scan — good for testing without setting up webhooks.

> ⚠️ **Drive push channels expire after 7 days.** Set a weekly calendar reminder
> to re-run `setup_watch.py`, or use the manual trigger via Zapier on a schedule.

---

### Step 6: Test It

1. Upload a short test video (.mp4) to your Evidence Videos Drive folder
2. Call the manual trigger:
   ```
   POST https://your-service.up.railway.app/analyze/folder
   ```
3. Watch Railway logs for processing progress
4. Check the Drive folder for `[filename]_ANALYSIS.txt`
5. Check `#customerservice` in Slack for the notification

---

## Zapier Integration (Alternative/Supplement to Drive Webhooks)

Since Drive webhooks expire, Zapier is a reliable alternative trigger:

**Zap: New File in Drive Folder → Trigger Analysis**
1. Trigger: Google Drive → New File in Folder → select your Evidence folder
2. Filter: File Type contains "video" (or no filter)
3. Action: Webhooks by Zapier → POST
   - URL: `https://your-service.up.railway.app/analyze/file/{{file_id}}`
   - Method: POST
   - No body needed

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Health check |
| `/webhook/drive` | POST | Google Drive push notification receiver |
| `/analyze/folder` | POST | Manually scan watch folder for new videos |
| `/analyze/file/{file_id}` | POST | Analyze a specific file by Drive ID |

---

## Analysis Output

The 10-section analysis covers:
1. **Incident Overview** — what, when, where, who
2. **Chronological Timeline** — timestamped event sequence
3. **Stop & Detention Analysis** — RAS/PC articulation, detention scope
4. **Search & Seizure Issues** — consent, warrant, inventory search
5. **Miranda & Statements** — rights given, invocations, suppressible statements
6. **Officer Conduct Flags** — use of force, coercion, protocol compliance
7. **Defense Favorable Observations** — all favorable facts
8. **Suppression Motion Indicators** — checklist of suppression grounds
9. **Gaps & Video Quality Notes** — missing footage, audio issues
10. **Recommended Follow-up** — action items for attorney/paralegal

---

## Costs (Approximate)

| Service | Cost | Per 30-min video |
|---|---|---|
| AssemblyAI | $0.37/hr audio | ~$0.19 |
| Claude API (claude-opus-4-5) | ~$0.015/1K tokens | ~$0.15–0.45 |
| Railway compute | ~$5–10/mo | — |
| **Total per video** | | **~$0.35–0.65** |

---

## Supported File Types

.mp4, .mov, .avi, .mkv, .webm, .mpg, .mpeg, .wmv, .3gp, .m4v

---

## Troubleshooting

**"Audio extraction failed"** — Check FFmpeg is installed in container (`docker run --rm llg-video ffmpeg -version`)

**"Transcription timed out"** — Video may be very long. AssemblyAI has a 10hr limit.

**"Drive watch channel not found"** — Channel may have expired. Re-run `setup_watch.py`.

**"GOOGLE_SERVICE_ACCOUNT_JSON error"** — Ensure the entire JSON is pasted as one line with no line breaks in Railway's variable editor.
