"""
CalendlyClient — Calendly API v2 Integration (REST)

Reads the firm's scheduled consultations so they can be surfaced (e.g. pushed to
Slack or a CRM). Uses a Personal Access Token — simplest auth, no OAuth dance,
ideal for a headless service.

Required env var:
    CALENDLY_API_TOKEN   — Personal Access Token from Calendly
                           (Integrations → API & Webhooks → Personal Access Tokens)

Leave it unset to disable this integration cleanly (no errors).
"""

import os
import logging
import aiohttp
from typing import List, Dict, Optional

log = logging.getLogger("calendly-client")

API_TOKEN = os.getenv("CALENDLY_API_TOKEN", "")
BASE_URL = "https://api.calendly.com"


def _configured() -> bool:
    return bool(API_TOKEN)


class CalendlyClient:

    def __init__(self):
        if not _configured():
            log.warning(
                "Calendly not configured — set CALENDLY_API_TOKEN to enable. "
                "Scheduling endpoints will return 'disabled'."
            )

    @property
    def enabled(self) -> bool:
        return _configured()

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        }

    async def _current_user_uri(self, session: aiohttp.ClientSession) -> Optional[str]:
        """Resolve the token owner's user URI (needed to scope event queries)."""
        async with session.get(f"{BASE_URL}/users/me", headers=self._headers()) as resp:
            body = await resp.json()
            if resp.status != 200:
                log.error(f"Calendly /users/me failed ({resp.status}): {body}")
                return None
            return body.get("resource", {}).get("uri")

    async def list_scheduled_events(self, count: int = 20, status: str = "active") -> List[Dict]:
        """
        Return upcoming/active scheduled events (consultations) for the token owner.
        Returns [] if the integration is disabled or the query fails.
        """
        if not self.enabled:
            log.info("Calendly disabled — skipping scheduled events")
            return []

        async with aiohttp.ClientSession() as session:
            user_uri = await self._current_user_uri(session)
            if not user_uri:
                return []

            params = {
                "user": user_uri,
                "count": str(min(count, 100)),
                "status": status,
                "sort": "start_time:asc",
            }
            async with session.get(
                f"{BASE_URL}/scheduled_events", headers=self._headers(), params=params
            ) as resp:
                body = await resp.json()
                if resp.status != 200:
                    log.error(f"Calendly scheduled_events failed ({resp.status}): {body}")
                    return []
                events = body.get("collection", [])
                log.info(f"Calendly: retrieved {len(events)} scheduled event(s)")
                return events

    async def list_event_invitees(self, event_uuid: str) -> List[Dict]:
        """Return invitees (name/email/answers) for a specific scheduled event."""
        if not self.enabled:
            return []

        url = f"{BASE_URL}/scheduled_events/{event_uuid}/invitees"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._headers()) as resp:
                body = await resp.json()
                if resp.status != 200:
                    log.error(f"Calendly invitees failed ({resp.status}): {body}")
                    return []
                return body.get("collection", [])
