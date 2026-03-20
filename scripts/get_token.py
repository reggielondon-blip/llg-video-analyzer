"""
get_token.py — One-time OAuth2 setup script
Run this ONCE on your local machine to generate a refresh token.
The refresh token lets the Railway server access all of Google Drive
as your Google account — no folder sharing required.

Usage:
    python scripts/get_token.py

Requirements:
    pip install google-auth-oauthlib

What it does:
    1. Opens a browser for you to log in with your Google account
    2. You grant Drive access
    3. Prints your GOOGLE_REFRESH_TOKEN to paste into Railway

You only need to run this once. The refresh token doesn't expire
unless you revoke access at myaccount.google.com/permissions.
"""

import os
import sys
import json

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Installing required package...")
    os.system(f"{sys.executable} -m pip install google-auth-oauthlib")
    from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive"]

def main():
    print("\n" + "="*60)
    print("  L & L Law Group — Google Drive OAuth Setup")
    print("="*60)
    print()

    # ── Get credentials from user ─────────────────────────────────
    print("You need your OAuth2 Client ID and Client Secret.")
    print("Get these from Google Cloud Console:")
    print("  → APIs & Services → Credentials → Create Credentials")
    print("  → OAuth 2.0 Client ID → Desktop Application")
    print()

    client_id = input("Paste your GOOGLE_CLIENT_ID: ").strip()
    if not client_id:
        print("❌ Client ID is required")
        sys.exit(1)

    client_secret = input("Paste your GOOGLE_CLIENT_SECRET: ").strip()
    if not client_secret:
        print("❌ Client Secret is required")
        sys.exit(1)

    print()
    print("Opening browser for Google login...")
    print("Log in with the Google account that owns the firm's Drive.")
    print()

    # ── Build client config ───────────────────────────────────────
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }

    # ── Run OAuth flow ────────────────────────────────────────────
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(
        port=0,
        prompt="consent",          # force showing consent to get refresh_token
        access_type="offline"
    )

    refresh_token = creds.refresh_token
    if not refresh_token:
        print()
        print("❌ No refresh token received.")
        print("   Try revoking access at myaccount.google.com/permissions")
        print("   then run this script again.")
        sys.exit(1)

    # ── Print results ─────────────────────────────────────────────
    print()
    print("="*60)
    print("  ✅ SUCCESS — Copy these 3 values into Railway Variables")
    print("="*60)
    print()
    print(f"GOOGLE_CLIENT_ID     = {client_id}")
    print(f"GOOGLE_CLIENT_SECRET = {client_secret}")
    print(f"GOOGLE_REFRESH_TOKEN = {refresh_token}")
    print()
    print("="*60)
    print("These replace GOOGLE_SERVICE_ACCOUNT_JSON in Railway.")
    print("Delete GOOGLE_SERVICE_ACCOUNT_JSON and DRIVE_WATCH_FOLDER_ID")
    print("from your Railway variables — they are no longer needed.")
    print("="*60)
    print()

    # Save locally as a convenience backup
    output = {
        "GOOGLE_CLIENT_ID": client_id,
        "GOOGLE_CLIENT_SECRET": client_secret,
        "GOOGLE_REFRESH_TOKEN": refresh_token
    }
    out_path = os.path.join(os.path.dirname(__file__), "google_credentials.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Credentials also saved to: {out_path}")
    print("⚠️  Do NOT commit google_credentials.json to GitHub.")


if __name__ == "__main__":
    main()
