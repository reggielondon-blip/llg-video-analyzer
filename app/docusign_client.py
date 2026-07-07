"""
DocuSignClient — DocuSign eSignature API Integration (REST)

Server-to-server access to DocuSign for automating documents like engagement
letters. Uses JWT Grant (impersonation) — the right flow for a headless service
with no interactive user login.

Required env vars:
    DOCUSIGN_INTEGRATION_KEY  — the app's integration key (client ID)
    DOCUSIGN_USER_ID          — GUID of the user to impersonate (API Username)
    DOCUSIGN_ACCOUNT_ID       — the DocuSign account (API Account) ID
    DOCUSIGN_PRIVATE_KEY      — the RSA private key (PEM). Literal "\\n" is accepted.
    DOCUSIGN_BASE_URL         — account base URI, e.g. https://demo.docusign.net
                                (demo) or https://na3.docusign.net (production)

Optional env var:
    DOCUSIGN_OAUTH_BASE       — OAuth host. Demo (default): account-d.docusign.com
                                Production: account.docusign.com

One-time setup note: JWT Grant requires admin consent for the app. Grant it once by
visiting the consent URL for your integration key with scope "signature impersonation".

Leave the env vars unset to disable this integration cleanly (no errors).
Requires PyJWT with the crypto extra (see requirements.txt) for RS256 signing.
"""

import os
import time
import base64
import logging
import aiohttp
from typing import Dict, List, Optional

log = logging.getLogger("docusign-client")

INTEGRATION_KEY = os.getenv("DOCUSIGN_INTEGRATION_KEY", "")
USER_ID         = os.getenv("DOCUSIGN_USER_ID", "")
ACCOUNT_ID      = os.getenv("DOCUSIGN_ACCOUNT_ID", "")
PRIVATE_KEY     = os.getenv("DOCUSIGN_PRIVATE_KEY", "").replace("\\n", "\n")
BASE_URL        = os.getenv("DOCUSIGN_BASE_URL", "").rstrip("/")
OAUTH_BASE      = os.getenv("DOCUSIGN_OAUTH_BASE", "account-d.docusign.com")

JWT_GRANT = "urn:ietf:params:oauth:grant-type:jwt-bearer"
TOKEN_LIFETIME = 3600  # seconds; DocuSign caps JWT assertion life at 1 hour


def _configured() -> bool:
    return all([INTEGRATION_KEY, USER_ID, ACCOUNT_ID, PRIVATE_KEY, BASE_URL])


class DocuSignClient:

    def __init__(self):
        if not _configured():
            log.warning(
                "DocuSign not configured — set DOCUSIGN_* env vars to enable. "
                "Envelope endpoints will return 'disabled'."
            )

    @property
    def enabled(self) -> bool:
        return _configured()

    def _build_assertion(self) -> Optional[str]:
        """Sign a short-lived JWT (RS256) for the JWT Grant flow."""
        try:
            import jwt  # PyJWT; RS256 needs the crypto extra
        except ImportError:
            log.error("PyJWT with crypto extra is required for DocuSign JWT auth")
            return None

        now = int(time.time())
        claims = {
            "iss": INTEGRATION_KEY,
            "sub": USER_ID,
            "aud": OAUTH_BASE,
            "iat": now,
            "exp": now + TOKEN_LIFETIME,
            "scope": "signature impersonation",
        }
        try:
            return jwt.encode(claims, PRIVATE_KEY, algorithm="RS256")
        except Exception as e:
            log.error(f"DocuSign JWT signing failed: {e}")
            return None

    async def _access_token(self, session: aiohttp.ClientSession) -> Optional[str]:
        assertion = self._build_assertion()
        if not assertion:
            return None
        data = {"grant_type": JWT_GRANT, "assertion": assertion}
        async with session.post(
            f"https://{OAUTH_BASE}/oauth/token", data=data
        ) as resp:
            body = await resp.json()
            if resp.status != 200:
                # A "consent_required" error here means the app hasn't been granted
                # admin consent yet — visit the consent URL once to fix it.
                log.error(f"DocuSign token exchange failed ({resp.status}): {body}")
                return None
            return body.get("access_token")

    async def list_envelopes(self, from_date: str = "2024-01-01") -> List[Dict]:
        """
        Return envelopes created since `from_date` (YYYY-MM-DD) with their status.
        Returns [] if disabled or on error.
        """
        if not self.enabled:
            log.info("DocuSign disabled — skipping envelope list")
            return []

        async with aiohttp.ClientSession() as session:
            token = await self._access_token(session)
            if not token:
                return []

            url = f"{BASE_URL}/restapi/v2.1/accounts/{ACCOUNT_ID}/envelopes"
            headers = {"Authorization": f"Bearer {token}"}
            params = {"from_date": from_date}
            async with session.get(url, headers=headers, params=params) as resp:
                body = await resp.json()
                if resp.status != 200:
                    log.error(f"DocuSign list envelopes failed ({resp.status}): {body}")
                    return []
                envelopes = body.get("envelopes", [])
                log.info(f"DocuSign: retrieved {len(envelopes)} envelope(s)")
                return envelopes

    async def send_document(
        self,
        signer_email: str,
        signer_name: str,
        document_b64: str,
        document_name: str = "Engagement Letter.pdf",
        subject: str = "Please sign: L & L Law Group",
    ) -> Dict:
        """
        Send a single PDF (base64-encoded) for signature with one signHere tab.
        Returns the API response dict, or {"error": ...} on failure.
        """
        if not self.enabled:
            return {"error": "disabled"}

        async with aiohttp.ClientSession() as session:
            token = await self._access_token(session)
            if not token:
                return {"error": "auth_failed"}

            envelope = {
                "emailSubject": subject,
                "status": "sent",
                "documents": [{
                    "documentBase64": document_b64,
                    "name": document_name,
                    "fileExtension": "pdf",
                    "documentId": "1",
                }],
                "recipients": {"signers": [{
                    "email": signer_email,
                    "name": signer_name,
                    "recipientId": "1",
                    "routingOrder": "1",
                    "tabs": {"signHereTabs": [{
                        "anchorString": "/sig/",
                        "anchorUnits": "pixels",
                        "anchorXOffset": "0",
                        "anchorYOffset": "0",
                    }]},
                }]},
            }
            url = f"{BASE_URL}/restapi/v2.1/accounts/{ACCOUNT_ID}/envelopes"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
            async with session.post(url, headers=headers, json=envelope) as resp:
                body = await resp.json()
                if resp.status not in (200, 201):
                    log.error(f"DocuSign send failed ({resp.status}): {body}")
                    return {"error": body}
                log.info(f"DocuSign: envelope sent to {signer_email}")
                return body
