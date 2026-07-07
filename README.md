# L & L Law Group — Case Video Analyzer

AI-powered analysis of body cam and in-car (dashcam) video evidence.
Watches a Google Drive folder, auto-processes new videos, and posts
a complete defense-focused legal analysis to Slack.

> **Integrations & developer-API reference:** see [`docs/INTEGRATIONS.md`](docs/INTEGRATIONS.md)
> for the full stack inventory, which services have developer APIs, and access steps.

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

Optional integrations (see **Google Ads API** and **RingCentral API** below):

| Variable | Value |
|---|---|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | 22-char token from your Ads manager (MCC) API Center |
| `GOOGLE_ADS_CLIENT_ID` | OAuth2 client ID (Google Cloud project) |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth2 client secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth2 refresh token |
| `GOOGLE_ADS_CUSTOMER_ID` | 10-digit account to query (no dashes) |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Manager (MCC) ID, no dashes (optional) |
| `GOOGLE_ADS_API_VERSION` | e.g. `v18` (optional; bump when calls 404) |
| `RINGCENTRAL_CLIENT_ID` | App Client ID from the Developer portal |
| `RINGCENTRAL_CLIENT_SECRET` | App Client Secret |
| `RINGCENTRAL_JWT` | Personal JWT credential (assertion string) |
| `RINGCENTRAL_SERVER_URL` | `https://platform.ringcentral.com` (prod) or the devtest URL (optional) |
| `CALENDLY_API_TOKEN` | Calendly Personal Access Token |
| `DOCUSIGN_INTEGRATION_KEY` | DocuSign app integration key (client ID) |
| `DOCUSIGN_USER_ID` | GUID of the user to impersonate (API Username) |
| `DOCUSIGN_ACCOUNT_ID` | DocuSign API account ID |
| `DOCUSIGN_PRIVATE_KEY` | RSA private key (PEM) |
| `DOCUSIGN_BASE_URL` | `https://demo.docusign.net` (demo) or your prod base URI |
| `DOCUSIGN_OAUTH_BASE` | `account-d.docusign.com` (demo) / `account.docusign.com` (prod) (optional) |

> Leave any of these unset to disable that integration cleanly — the service
> starts fine and the related endpoints simply return `{"status": "disabled"}`.

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
| `/health` | GET | Health check (includes integration status) |
| `/webhook/drive` | POST | Google Drive push notification receiver |
| `/analyze/folder` | POST | Manually scan watch folder for new videos |
| `/analyze/file/{file_id}` | POST | Analyze a specific file by Drive ID |
| `/ads/report?days=30` | GET | Google Ads per-campaign performance (if configured) |
| `/calls/log?per_page=100` | GET | RingCentral recent call log (if configured) |
| `/calendly/events?count=20` | GET | Upcoming Calendly consultations (if configured) |
| `/docs/envelopes?from_date=YYYY-MM-DD` | GET | DocuSign envelope statuses (if configured) |

---

## Optional: Google Ads API

Pulls campaign performance (impressions, clicks, cost, conversions) for the
firm's lead-gen accounts. Getting access is a multi-step approval — budget a
few days for Google's review.

**What to request / set up:**

1. **A Google Ads Manager account (MCC)** — the developer token is issued at the
   *manager* level, not a regular Ads account. Create one (free) and link your
   Ads account under it if you don't have one.
2. **A developer token** — apply at [ads.google.com/aw/apicenter](https://ads.google.com/aw/apicenter) →
   complete the API Access form → accept the Terms. Google checks that your
   company website is live and that the API contact email is monitored.
   Request **Basic access** (production, 15,000 ops/day) — plenty for reporting.
   Google may require **brand verification** on your Cloud project to approve it.
3. **OAuth2 credentials** — in your Google Cloud project (you can reuse the one
   from the Drive setup), create an OAuth2 **Client ID + Client Secret**.
4. **A refresh token** — run the OAuth2 consent flow once to mint it so the
   service can authenticate without a login prompt.
5. **Your Customer ID** — the 10-digit ID of the account to query.

Set the `GOOGLE_ADS_*` variables above. Test with `GET /ads/report?days=30`.

---

## Optional: RingCentral API

Server-to-server access to the firm's phone system — pull the call log and send
SMS. Uses **JWT auth**, ideal for a headless service (no login UI needed).

**What to request / set up:**

1. **A RingCentral Developer account** — sign in at
   [developers.ringcentral.com](https://developers.ringcentral.com) using the
   **same login as your production RingCentral account** (a dev-portal-only
   account won't reach your real data).
2. **Admin permission** — if the "Create App" button is greyed out, your
   RingCentral **administrator** must grant app-creation permission.
3. **A REST API App** — Console → Apps → Create App → **REST API App**. On
   creation you get a **Client ID + Client Secret** for sandbox and production.
4. **JWT auth + scopes** — choose JWT auth and select the scopes you need
   (`ReadCallLog` for the call log, `SMS` to send texts). Fewer scopes graduate
   faster.
5. **A personal JWT credential** — generate it in the portal; paste it as
   `RINGCENTRAL_JWT`.
6. **Graduate to production** — apps start in sandbox; submit for production
   approval to use real account data (set `RINGCENTRAL_SERVER_URL` accordingly).

Set the `RINGCENTRAL_*` variables above. Test with `GET /calls/log`.

---

## Optional: Calendly API

Reads upcoming consultations so they can be surfaced (e.g. to Slack). Uses a
Personal Access Token — no OAuth flow.

**What to request / set up:**

1. Sign in to Calendly → **Integrations → API & Webhooks → Personal Access Tokens**.
2. Generate a token and paste it as `CALENDLY_API_TOKEN`.

Test with `GET /calendly/events?count=20`.

---

## Optional: DocuSign eSignature API

Automates documents like engagement letters. Uses **JWT Grant** (impersonation) —
the right flow for a headless service.

**What to request / set up:**

1. **A DocuSign developer account** — [developers.docusign.com](https://developers.docusign.com)
   (starts in the demo environment).
2. **An app + integration key** — Admin → Apps and Keys → Add App. Note the
   **integration key** and your **API account ID**.
3. **An RSA keypair** — generate it on the app; keep the **private key** for
   `DOCUSIGN_PRIVATE_KEY`.
4. **Your API user ID** — the GUID (API Username) of the user to impersonate.
5. **Grant admin consent (one-time)** — visit the consent URL for your integration
   key with scope `signature impersonation` and approve, or JWT auth returns
   `consent_required`.
6. **Go live** — promote the app from demo to production and switch
   `DOCUSIGN_BASE_URL` / `DOCUSIGN_OAUTH_BASE` to the production hosts.

Set the `DOCUSIGN_*` variables above. Test with `GET /docs/envelopes`.

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
