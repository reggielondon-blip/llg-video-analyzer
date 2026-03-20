"""
Transcriber — AssemblyAI Integration
Uses speaker diarization to separate officer vs. subject speech,
which is critical for body cam and in-car video evidence analysis.
"""

import os
import asyncio
import logging
import aiohttp
import aiofiles
from typing import Optional

log = logging.getLogger("transcriber")

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY", "")
UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"
POLL_INTERVAL = 5   # seconds between status checks
TIMEOUT = 1800      # 30 min max wait for long videos


class Transcriber:

    def __init__(self):
        if not ASSEMBLYAI_API_KEY:
            log.warning("ASSEMBLYAI_API_KEY not set — transcription will be skipped")
        self.headers = {
            "authorization": ASSEMBLYAI_API_KEY,
            "content-type": "application/json"
        }

    async def transcribe(self, audio_path: str) -> str:
        """
        Full pipeline: upload audio → request transcript → poll → return text.
        Returns formatted transcript with speaker labels if diarization succeeds.
        Falls back to plain text if diarization fails.
        """
        if not ASSEMBLYAI_API_KEY:
            return "[Transcription skipped — ASSEMBLYAI_API_KEY not configured]"

        file_size_mb = os.path.getsize(audio_path) / (1024 * 1024)
        log.info(f"Uploading audio ({file_size_mb:.1f}MB) to AssemblyAI...")

        async with aiohttp.ClientSession() as session:
            # ── Step 1: Upload audio file ─────────────────────────────────
            upload_url = await self._upload_file(session, audio_path)
            if not upload_url:
                return "[Audio upload failed]"

            # ── Step 2: Request transcription with diarization ────────────
            transcript_id = await self._request_transcript(session, upload_url)
            if not transcript_id:
                return "[Transcription request failed]"

            log.info(f"Transcription job started: {transcript_id}")

            # ── Step 3: Poll for completion ───────────────────────────────
            result = await self._poll_for_result(session, transcript_id)

        return self._format_transcript(result)

    async def _upload_file(
        self, session: aiohttp.ClientSession, audio_path: str
    ) -> Optional[str]:
        """Upload audio bytes to AssemblyAI and return the hosted URL."""
        try:
            async with aiofiles.open(audio_path, "rb") as f:
                audio_data = await f.read()

            headers = {"authorization": ASSEMBLYAI_API_KEY}
            async with session.post(
                UPLOAD_URL, data=audio_data, headers=headers
            ) as resp:
                if resp.status != 200:
                    log.error(f"Upload failed: {resp.status}")
                    return None
                data = await resp.json()
                return data.get("upload_url")
        except Exception as e:
            log.error(f"Upload error: {e}", exc_info=True)
            return None

    async def _request_transcript(
        self, session: aiohttp.ClientSession, audio_url: str
    ) -> Optional[str]:
        """Submit transcription job with speaker diarization enabled."""
        payload = {
            "audio_url": audio_url,
            "speaker_labels": True,          # distinguish officer vs. suspect
            "speakers_expected": 3,           # officer, subject, bystanders
            "punctuate": True,
            "format_text": True,
            "language_detection": True,       # handles Spanish-speaking clients
            "disfluencies": False,            # remove ums/uhs for cleaner output
            "filter_profanity": False,        # preserve exact speech for evidence
            # Boost recognition of legal/law enforcement terms
            "word_boost": [
                "Miranda", "arrest", "warrant", "officer", "license",
                "registration", "weapon", "firearm", "hands", "vehicle",
                "defendant", "suspect", "detain", "search", "probable cause"
            ],
            "boost_param": "high"
        }
        try:
            async with session.post(
                TRANSCRIPT_URL, json=payload, headers=self.headers
            ) as resp:
                if resp.status != 200:
                    body = await resp.text()
                    log.error(f"Transcript request failed {resp.status}: {body}")
                    return None
                data = await resp.json()
                return data.get("id")
        except Exception as e:
            log.error(f"Transcript request error: {e}", exc_info=True)
            return None

    async def _poll_for_result(
        self, session: aiohttp.ClientSession, transcript_id: str
    ) -> dict:
        """Poll until transcription is complete or times out."""
        elapsed = 0
        while elapsed < TIMEOUT:
            await asyncio.sleep(POLL_INTERVAL)
            elapsed += POLL_INTERVAL
            try:
                async with session.get(
                    f"{TRANSCRIPT_URL}/{transcript_id}",
                    headers=self.headers
                ) as resp:
                    data = await resp.json()
                    status = data.get("status")
                    log.debug(f"Transcript status: {status} ({elapsed}s elapsed)")

                    if status == "completed":
                        log.info(f"Transcription complete ({elapsed}s)")
                        return data
                    elif status == "error":
                        log.error(f"Transcription error: {data.get('error')}")
                        return data
                    # Still processing: 'queued' or 'processing'
            except Exception as e:
                log.warning(f"Poll error (will retry): {e}")

        log.error(f"Transcription timed out after {TIMEOUT}s")
        return {"status": "timeout", "text": "", "utterances": []}

    def _format_transcript(self, result: dict) -> str:
        """
        Format the transcript with speaker labels.
        Falls back gracefully if diarization data is missing.
        """
        status = result.get("status", "unknown")

        if status == "timeout":
            return "[Transcription timed out — video may be too long]"

        if status == "error":
            return f"[Transcription failed: {result.get('error', 'unknown error')}]"

        # Prefer utterance-level (speaker-labeled) format
        utterances = result.get("utterances") or []
        if utterances:
            lines = []
            for u in utterances:
                speaker = f"SPEAKER {u.get('speaker', '?')}"
                text = u.get("text", "").strip()
                start_ms = u.get("start", 0)
                timestamp = self._ms_to_timestamp(start_ms)
                lines.append(f"[{timestamp}] {speaker}: {text}")
            return "\n".join(lines)

        # Fallback: plain text
        return result.get("text", "[No transcript available]") or "[Empty transcript]"

    @staticmethod
    def _ms_to_timestamp(ms: int) -> str:
        seconds = ms // 1000
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02d}:{secs:02d}"
