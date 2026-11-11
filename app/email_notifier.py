"""
EmailNotifier — Sends analysis alerts using SMTP or the configured Zapier HTTPS route.
Zapier uses the existing Gmail connection and does not need a Gmail app password.

Required env vars:
    NOTIFY_EMAIL_FROM     — Gmail address sending the notification
    NOTIFY_EMAIL_PASSWORD — Gmail App Password (16-char, not account password)
    NOTIFY_EMAIL_TO       — Where to send alerts (e.g. info@landllawgroup.com)
"""

import os
import asyncio
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from app.email_transport import ZapierEmailTransport, NotificationError

log = logging.getLogger("email-notifier")

FROM_EMAIL = os.getenv("NOTIFY_EMAIL_FROM", "")
PASSWORD   = os.getenv("NOTIFY_EMAIL_PASSWORD", "")
TO_EMAIL   = os.getenv("NOTIFY_EMAIL_TO", "info@landllawgroup.com")
TRANSPORT = os.getenv("NOTIFY_EMAIL_TRANSPORT", "smtp").strip().lower()
ZAPIER_URL = os.getenv("ZAPIER_MCP_URL", "")
ZAPIER_CONNECTION = os.getenv("NOTIFY_ZAPIER_CONNECTION_ID", "")


def _configured():
    if TRANSPORT == "zapier":
        return all([FROM_EMAIL, TO_EMAIL, ZAPIER_URL, ZAPIER_CONNECTION])
    if TRANSPORT == "smtp":
        return all([FROM_EMAIL, TO_EMAIL, PASSWORD])
    raise NotificationError("Unsupported email transport")


class EmailNotifier:

    def __init__(self):
        if not _configured():
            log.warning("Email transport is not fully configured — notifications disabled")

    async def post_analysis_complete(
        self,
        file_name: str,
        summary: str,
        drive_link: str,
        duration_seconds: float,
        transcript_chars: int
    ):
        if not _configured():
            log.info("Email not configured — skipping notification")
            return

        duration_str = _format_duration(duration_seconds)
        preview      = _extract_preview(summary)
        timestamp    = datetime.now().strftime("%B %d, %Y at %I:%M %p")

        subject = f"[L&L] Video Analysis Ready — {file_name}"

        body = f"""L & L Law Group — Case Video Analysis Complete
{'='*60}

File:       {file_name}
Duration:   {duration_str}
Transcript: {'Available' if transcript_chars > 50 else 'Not available (silent or audio issue)'}
Completed:  {timestamp}

VIEW FULL ANALYSIS:
{drive_link}

{'='*60}
INCIDENT OVERVIEW (PREVIEW):
{preview}

{'='*60}
The full 10-section analysis is saved to Google Drive at the link above.
Sections covered: Stop & Detention, Search & Seizure, Miranda & Statements,
Officer Conduct, Defense Observations, Suppression Motion Indicators,
and Recommended Follow-up Actions.

— L & L Law Group Case Video Analyzer
"""

        return await asyncio.to_thread(_send, subject, body)

    async def post_error(self, file_id: str, error: str):
        if not _configured():
            return
        subject = f"[L&L] Video Analyzer Error — File {file_id[:12]}..."
        body    = f"""L & L Law Group — Video Analyzer Error

File ID: {file_id}
Error:   {error[:500]}

Check Railway logs for full details.
Service URL: https://railway.app
"""
        return await asyncio.to_thread(_send, subject, body)


def _send(subject: str, body: str):
    try:
        if not _configured():
            log.warning("Email transport not configured; nothing sent")
            return None
        if TRANSPORT == "zapier":
            receipt = ZapierEmailTransport(ZAPIER_URL, ZAPIER_CONNECTION, FROM_EMAIL, TO_EMAIL).send(subject, body)
            log.info("Email accepted by Gmail via HTTPS; message_id=%s", receipt)
            return receipt
        msg = MIMEMultipart()
        msg["From"]    = FROM_EMAIL
        msg["To"]      = TO_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

        log.info(f"Email sent to {TO_EMAIL}: {subject}")
        return True
    except NotificationError as e:
        log.error("Email notification failed: %s", e)
        return None
    except Exception as e:
        log.error("Email notification failed (%s); not retried", type(e).__name__)
        return None


def _format_duration(seconds: float) -> str:
    if seconds <= 0:
        return "Unknown"
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m {secs}s"
    return f"{minutes}m {secs}s"


def _extract_preview(summary: str, max_chars: int = 600) -> str:
    try:
        marker = "1. INCIDENT OVERVIEW"
        start  = summary.find(marker)
        if start == -1:
            return summary[:max_chars]
        section = summary[start + len(marker):]
        end     = section.find("\n2.")
        preview = section[:end].strip() if end != -1 else section[:max_chars].strip()
        return preview[:max_chars] + ("..." if len(preview) > max_chars else "")
    except Exception:
        return summary[:max_chars]
