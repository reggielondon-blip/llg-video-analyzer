"""Auth and input limits for optional Ads, phone, calendar, and DocuSign reads."""

import hmac
import os
import re

TOKEN = os.getenv("INTEGRATIONS_API_TOKEN", "")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def auth_status(authorization: str | None) -> str:
    """Return ok, unconfigured, or unauthorized.

    Integration reads stay closed until INTEGRATIONS_API_TOKEN is set and the
    caller sends it as Authorization: Bearer <token>.
    """
    if not TOKEN:
        return "unconfigured"
    if authorization is None or not authorization.startswith("Bearer "):
        return "unauthorized"
    given = authorization[len("Bearer "):]
    if len(given) != len(TOKEN):
        return "unauthorized"
    if not hmac.compare_digest(given, TOKEN):
        return "unauthorized"
    return "ok"


def clamp_int(value: int, low: int, high: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return low
    return max(low, min(high, number))


def valid_date(value: str) -> bool:
    return bool(DATE.match(value or ""))
