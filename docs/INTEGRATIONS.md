# L & L Law Group — Integrations & Developer-API Reference

A single reference for the firm's technology stack: what each service does, whether
it has a **developer API** you can build against, and — for the ones we're actively
wiring in — exactly what to request to get access.

- **✅ Wired in** = integrated in this app today
- **🔨 Added, needs credentials** = code is in the repo but inert until tokens are set
- **🔌 Connected to Claude** = available as a Claude connector; can also be built against directly
- **⚠️ Needs authorization** = connector requires an OAuth step in claude.ai settings before use

---

## 1. In this app today (code + README)

| Service | Role in the app | Developer API |
|---|---|---|
| **Anthropic Claude** | 10-section legal analysis | ✅ Full REST API |
| **AssemblyAI** | Transcription + speaker diarization | ✅ REST API |
| **Google Drive** | Video watch folder + analysis output | ✅ Drive API (service account) |
| **Slack** | Notifications | ✅ Web API + incoming webhooks |
| **Gmail (SMTP)** | Email alerts on completion | ✅ SMTP + Gmail API |
| **Railway** | Hosting / deploy | ✅ GraphQL API |
| **FastAPI / FFmpeg** | Web framework / media processing | n/a (libraries, not services) |

## 2. Added in this branch — need credentials

| Service | New capability | Auth | Status |
|---|---|---|---|
| **Google Ads** | Per-campaign performance reporting (`/ads/report`) | OAuth2 refresh token | 🔨 needs dev token + tokens |
| **RingCentral** | Call log + SMS (`/calls/log`) | JWT | 🔨 needs app + JWT credential |

Access steps for these two are in Sections 5–6 below.

## 3. Connected to your Claude workspace

Everything hooked up to your Claude environment. Almost all have public developer
APIs you could integrate into this service the same way we did Google Ads / RingCentral.

| Connector | Use for the firm | Developer API |
|---|---|---|
| **GitHub** | Code / repos | ✅ REST + GraphQL |
| **Zapier** | Automation glue (6,000+ apps) | ✅ + connectors |
| **Netlify** | Web hosting | ✅ REST API |
| **Canva** | Marketing / design assets | ✅ Connect APIs |
| **Calendly** | Consultation scheduling | ✅ REST API |
| **Google Calendar** | Scheduling | ✅ Google API |
| **Google Drive** | Documents / evidence | ✅ Google API |
| **Gmail** | Email | ✅ Google API |
| **Slack** | Team comms | ✅ Web API |
| **DocuSign** | E-signature (engagement letters) | ✅ eSignature REST API — ⚠️ needs authorization |
| **Ahrefs** | SEO / marketing analytics | ✅ API v3 |
| **Adzviser** | Ad reporting (Google/FB/etc.) | ⚠️ Primarily a reporting connector |
| **Blotato** | Social-media posting | ✅ API |
| **Midpage** | Legal research | ✅ API / MCP |
| **Plaud** | AI voice recorder / notes | ⚠️ Newer/limited API — needs authorization |

> **⚠️ DocuSign** and **Plaud** must be authorized in your claude.ai connector
> settings before they can be used from an automated session.

## 4. "What has developer-API capabilities?" — the short answer

**Strong, well-documented APIs — good candidates to build into this service:**

- **Marketing / lead-gen:** Google Ads, Ahrefs, Canva, Calendly
- **Client comms:** RingCentral, Slack, Gmail, Blotato
- **Legal ops:** DocuSign (signatures), Midpage (research), Google Drive
- **Infrastructure:** GitHub, Railway, Netlify, Zapier (catch-all bridge)

**Connector-only / thin for direct integration:** Adzviser, Plaud.

**Recommended next building blocks** (given the lead-gen + calls direction):
**DocuSign** (automate engagement letters) and **Calendly** (consultation booking →
Slack/CRM). Both slot into the same env-var + optional-endpoint pattern already used
in the app.

---

## 5. Getting access: Google Ads API

Pulls campaign performance (impressions, clicks, cost, conversions) for the firm's
lead-gen accounts. Multi-step approval — budget a few days for Google's review.

**What to request / set up:**

1. **Google Ads Manager account (MCC)** — the developer token is issued at the
   *manager* level, not a regular Ads account. Create one (free) and link your Ads
   account under it.
2. **Developer token** — apply at [ads.google.com/aw/apicenter](https://ads.google.com/aw/apicenter),
   complete the API Access form, accept the Terms. Google checks your company website
   is live and the API contact email is monitored. Request **Basic access**
   (production, 15,000 ops/day). Brand verification on your Cloud project may be
   required to approve it.
3. **OAuth2 credentials** — Client ID + Secret in your Google Cloud project (reuse the
   Drive one).
4. **Refresh token** — run the OAuth2 consent flow once so the service authenticates
   without a login prompt.
5. **Customer ID** — the 10-digit ID of the account to query.

**Env vars:** `GOOGLE_ADS_DEVELOPER_TOKEN`, `GOOGLE_ADS_CLIENT_ID`,
`GOOGLE_ADS_CLIENT_SECRET`, `GOOGLE_ADS_REFRESH_TOKEN`, `GOOGLE_ADS_CUSTOMER_ID`,
optional `GOOGLE_ADS_LOGIN_CUSTOMER_ID`, `GOOGLE_ADS_API_VERSION`. Test with
`GET /ads/report?days=30`.

## 6. Getting access: RingCentral API

Server-to-server access to the firm's phone system — call log and SMS. JWT auth,
ideal for a headless service.

**What to request / set up:**

1. **Developer account** — sign in at [developers.ringcentral.com](https://developers.ringcentral.com)
   with your **production RingCentral login** (a dev-portal-only account won't reach
   real data).
2. **Admin permission** — if "Create App" is greyed out, your RingCentral
   administrator must grant app-creation permission.
3. **REST API App** — Console → Apps → Create App → REST API App. Yields Client ID +
   Secret for sandbox and production.
4. **JWT auth + scopes** — choose JWT; select `ReadCallLog` (call log) and `SMS` (send
   texts). Fewer scopes graduate faster.
5. **Personal JWT credential** — generate in the portal; paste as `RINGCENTRAL_JWT`.
6. **Graduate to production** — apps start in sandbox; submit for production approval,
   then set `RINGCENTRAL_SERVER_URL` accordingly.

**Env vars:** `RINGCENTRAL_CLIENT_ID`, `RINGCENTRAL_CLIENT_SECRET`, `RINGCENTRAL_JWT`,
optional `RINGCENTRAL_SERVER_URL`. Test with `GET /calls/log`.

---

## 7. How new integrations plug in

Every integration in this app follows the same pattern, so adding more is mechanical:

1. A client module in `app/` (REST via `aiohttp`), driven by env vars.
2. **Graceful degradation** — unset env vars disable the integration; the service still
   starts and the endpoint returns `{"status": "disabled"}`.
3. Optional read-only endpoint(s) in `main.py`, with status surfaced on `/health`.
4. Env vars + an access section documented here and in the README.
