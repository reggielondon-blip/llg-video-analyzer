"""
setup_watch.py — One-time script to register a Google Drive push notification
channel on your evidence video folder.

Run this locally or on Railway with:
    python scripts/setup_watch.py

Required env vars:
    GOOGLE_SERVICE_ACCOUNT_JSON
    DRIVE_WATCH_FOLDER_ID
    RAILWAY_PUBLIC_URL  (or set WEBHOOK_BASE_URL manually)

Drive push channels expire after 7 days max. Re-run this script weekly,
or set up a Railway cron job to call /webhook/renew.
"""

import os
import sys
import json
import uuid

# Add parent dir to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    # Load env
    folder_id = os.getenv("DRIVE_WATCH_FOLDER_ID")
    if not folder_id:
        print("❌ DRIVE_WATCH_FOLDER_ID not set")
        sys.exit(1)

    base_url = os.getenv("WEBHOOK_BASE_URL") or os.getenv("RAILWAY_PUBLIC_URL")
    if not base_url:
        print("❌ Set WEBHOOK_BASE_URL to your Railway service URL")
        print("   e.g. https://your-service.up.railway.app")
        sys.exit(1)

    base_url = base_url.rstrip("/")
    webhook_url = f"{base_url}/webhook/drive"
    channel_id = str(uuid.uuid4())

    print(f"\n📁 Folder ID:   {folder_id}")
    print(f"🔗 Webhook URL: {webhook_url}")
    print(f"🔑 Channel ID:  {channel_id}")
    print()

    # Import after env is confirmed
    from app.drive_client import DriveClient
    client = DriveClient()

    try:
        response = client.setup_folder_watch(
            folder_id=folder_id,
            webhook_url=webhook_url,
            channel_id=channel_id,
            expiration_hours=168  # 7 days
        )
        print("✅ Watch channel created successfully!")
        print(json.dumps(response, indent=2))
        print()
        print("⚠️  IMPORTANT: Save these values for renewal/cancellation:")
        print(f"   Channel ID:   {response.get('id')}")
        print(f"   Resource ID:  {response.get('resourceId')}")
        print(f"   Expires:      {response.get('expiration')} ms (Unix)")
        print()
        print("📅 This channel expires in 7 days. Set a calendar reminder to re-run.")

    except Exception as e:
        print(f"❌ Failed to create watch channel: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Load .env file if present (local dev)
    env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    main()
