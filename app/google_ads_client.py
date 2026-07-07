"""
GoogleAdsClient — Google Ads API Integration (REST)

Pulls campaign performance (impressions, clicks, cost, conversions) for the
firm's lead-gen ad accounts. Uses OAuth2 refresh-token auth over the REST
searchStream endpoint — no heavy client library, consistent with the rest of
this service (aiohttp only).

Required env vars:
    GOOGLE_ADS_DEVELOPER_TOKEN    — 22-char token from your Ads manager (MCC) API Center
    GOOGLE_ADS_CLIENT_ID          — OAuth2 client ID (Google Cloud project)
    GOOGLE_ADS_CLIENT_SECRET      — OAuth2 client secret
    GOOGLE_ADS_REFRESH_TOKEN      — OAuth2 refresh token (generated once via the consent flow)
    GOOGLE_ADS_CUSTOMER_ID        — 10-digit ID of the account to query (no dashes)

Optional env vars:
    GOOGLE_ADS_LOGIN_CUSTOMER_ID  — manager (MCC) ID, no dashes. Required only when
                                    the account above is accessed via a manager account.
    GOOGLE_ADS_API_VERSION        — API version segment, e.g. "v18". Google deprecates
                                    versions ~yearly; bump this when calls start 404ing.

Leave the env vars unset to disable this integration cleanly (no errors).
"""

import os
import logging
import aiohttp
from typing import List, Dict, Optional

log = logging.getLogger("google-ads-client")

DEVELOPER_TOKEN   = os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN", "")
CLIENT_ID         = os.getenv("GOOGLE_ADS_CLIENT_ID", "")
CLIENT_SECRET     = os.getenv("GOOGLE_ADS_CLIENT_SECRET", "")
REFRESH_TOKEN     = os.getenv("GOOGLE_ADS_REFRESH_TOKEN", "")
CUSTOMER_ID       = os.getenv("GOOGLE_ADS_CUSTOMER_ID", "").replace("-", "")
LOGIN_CUSTOMER_ID = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").replace("-", "")
API_VERSION       = os.getenv("GOOGLE_ADS_API_VERSION", "v18")

TOKEN_URL = "https://oauth2.googleapis.com/token"

# Micros → currency: Google Ads reports monetary values in micros (1e6 == 1 unit).
MICROS = 1_000_000


def _configured() -> bool:
    return all([DEVELOPER_TOKEN, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, CUSTOMER_ID])


class GoogleAdsClient:

    def __init__(self):
        if not _configured():
            log.warning(
                "Google Ads not configured — set GOOGLE_ADS_* env vars to enable. "
                "Reporting endpoints will return 'disabled'."
            )

    @property
    def enabled(self) -> bool:
        return _configured()

    async def _access_token(self, session: aiohttp.ClientSession) -> Optional[str]:
        """Exchange the long-lived refresh token for a short-lived access token."""
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": REFRESH_TOKEN,
            "grant_type": "refresh_token",
        }
        async with session.post(TOKEN_URL, data=data) as resp:
            body = await resp.json()
            if resp.status != 200:
                log.error(f"Google Ads token exchange failed ({resp.status}): {body}")
                return None
            return body.get("access_token")

    async def get_campaign_performance(self, days: int = 30) -> List[Dict]:
        """
        Return per-campaign performance for the trailing `days` window.

        Each row: campaign name/id/status + impressions, clicks, cost, conversions.
        Returns [] if the integration is disabled or the query fails.
        """
        if not self.enabled:
            log.info("Google Ads disabled — skipping campaign report")
            return []

        query = (
            "SELECT campaign.id, campaign.name, campaign.status, "
            "metrics.impressions, metrics.clicks, metrics.cost_micros, "
            "metrics.conversions, metrics.conversions_value "
            "FROM campaign "
            f"WHERE segments.date DURING LAST_{_valid_range(days)} "
            "ORDER BY metrics.cost_micros DESC"
        )

        async with aiohttp.ClientSession() as session:
            token = await self._access_token(session)
            if not token:
                return []

            url = (
                f"https://googleads.googleapis.com/{API_VERSION}"
                f"/customers/{CUSTOMER_ID}/googleAds:searchStream"
            )
            headers = {
                "Authorization": f"Bearer {token}",
                "developer-token": DEVELOPER_TOKEN,
                "Content-Type": "application/json",
            }
            if LOGIN_CUSTOMER_ID:
                headers["login-customer-id"] = LOGIN_CUSTOMER_ID

            async with session.post(url, headers=headers, json={"query": query}) as resp:
                body = await resp.json()
                if resp.status != 200:
                    log.error(f"Google Ads query failed ({resp.status}): {body}")
                    return []
                return _parse_campaign_rows(body)


def _valid_range(days: int) -> str:
    """Map a day count to a Google Ads GAQL relative date literal."""
    if days <= 7:
        return "7_DAYS"
    if days <= 14:
        return "14_DAYS"
    return "30_DAYS"


def _parse_campaign_rows(body) -> List[Dict]:
    """searchStream returns a list of response chunks, each with a 'results' array."""
    rows: List[Dict] = []
    chunks = body if isinstance(body, list) else [body]
    for chunk in chunks:
        for result in chunk.get("results", []):
            campaign = result.get("campaign", {})
            metrics = result.get("metrics", {})
            rows.append({
                "campaign_id": campaign.get("id"),
                "campaign_name": campaign.get("name"),
                "status": campaign.get("status"),
                "impressions": int(metrics.get("impressions", 0)),
                "clicks": int(metrics.get("clicks", 0)),
                "cost": round(int(metrics.get("costMicros", 0)) / MICROS, 2),
                "conversions": round(float(metrics.get("conversions", 0)), 2),
                "conversions_value": round(float(metrics.get("conversionsValue", 0)), 2),
            })
    log.info(f"Google Ads: retrieved {len(rows)} campaign row(s)")
    return rows
