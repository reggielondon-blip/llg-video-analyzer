"""
RingCentralClient — RingCentral API Integration (REST)

Server-to-server access to the firm's phone system: pull the call log and send
SMS. Uses JWT auth (the "personal JWT credential" you generate in the RingCentral
Developer portal) — ideal for a headless service like this one, no user login UI.

Required env vars:
    RINGCENTRAL_CLIENT_ID       — app Client ID from the Developer portal
    RINGCENTRAL_CLIENT_SECRET   — app Client Secret
    RINGCENTRAL_JWT             — personal JWT credential (the assertion string)

Optional env vars:
    RINGCENTRAL_SERVER_URL      — production: https://platform.ringcentral.com (default)
                                  sandbox:    https://platform.devtest.ringcentral.com

Leave the env vars unset to disable this integration cleanly (no errors).

Required app scopes (set when creating the app):
    ReadCallLog   — for get_call_log()
    SMS           — for send_sms()
"""

import os
import base64
import logging
import aiohttp
from typing import List, Dict, Optional

log = logging.getLogger("ringcentral-client")

CLIENT_ID     = os.getenv("RINGCENTRAL_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("RINGCENTRAL_CLIENT_SECRET", "")
JWT           = os.getenv("RINGCENTRAL_JWT", "")
SERVER_URL    = os.getenv("RINGCENTRAL_SERVER_URL", "https://platform.ringcentral.com").rstrip("/")

JWT_GRANT = "urn:ietf:params:oauth:grant-type:jwt-bearer"


def _configured() -> bool:
    return all([CLIENT_ID, CLIENT_SECRET, JWT])


class RingCentralClient:

    def __init__(self):
        if not _configured():
            log.warning(
                "RingCentral not configured — set RINGCENTRAL_* env vars to enable. "
                "Call-log / SMS features will return 'disabled'."
            )

    @property
    def enabled(self) -> bool:
        return _configured()

    async def _access_token(self, session: aiohttp.ClientSession) -> Optional[str]:
        """Exchange the JWT credential for a short-lived access token."""
        basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": JWT_GRANT, "assertion": JWT}
        async with session.post(
            f"{SERVER_URL}/restapi/oauth/token", headers=headers, data=data
        ) as resp:
            body = await resp.json()
            if resp.status != 200:
                log.error(f"RingCentral token exchange failed ({resp.status}): {body}")
                return None
            return body.get("access_token")

    async def get_call_log(self, per_page: int = 100, view: str = "Simple") -> List[Dict]:
        """
        Return recent call-log records for the authenticated extension.
        Requires the ReadCallLog scope. Returns [] if disabled or on error.
        """
        if not self.enabled:
            log.info("RingCentral disabled — skipping call log")
            return []

        async with aiohttp.ClientSession() as session:
            token = await self._access_token(session)
            if not token:
                return []

            url = f"{SERVER_URL}/restapi/v1.0/account/~/extension/~/call-log"
            headers = {"Authorization": f"Bearer {token}"}
            params = {"perPage": str(per_page), "view": view}
            async with session.get(url, headers=headers, params=params) as resp:
                body = await resp.json()
                if resp.status != 200:
                    log.error(f"RingCentral call-log failed ({resp.status}): {body}")
                    return []
                records = body.get("records", [])
                log.info(f"RingCentral: retrieved {len(records)} call-log record(s)")
                return records

    async def send_sms(self, to_number: str, from_number: str, text: str) -> Dict:
        """
        Send an SMS. Requires the SMS scope. `from_number` must be an
        SMS-enabled number on the account (E.164, e.g. +12145551234).
        Returns the API response dict, or {"error": ...} on failure.
        """
        if not self.enabled:
            log.info("RingCentral disabled — skipping SMS")
            return {"error": "disabled"}

        async with aiohttp.ClientSession() as session:
            token = await self._access_token(session)
            if not token:
                return {"error": "auth_failed"}

            url = f"{SERVER_URL}/restapi/v1.0/account/~/extension/~/sms"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
            payload = {
                "from": {"phoneNumber": from_number},
                "to": [{"phoneNumber": to_number}],
                "text": text,
            }
            async with session.post(url, headers=headers, json=payload) as resp:
                body = await resp.json()
                if resp.status not in (200, 201):
                    log.error(f"RingCentral SMS failed ({resp.status}): {body}")
                    return {"error": body}
                log.info(f"RingCentral: SMS sent to {to_number}")
                return body
