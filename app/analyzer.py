"""
VideoAnalyzer — Claude API Integration
Criminal defense-focused analysis of body cam and in-car video evidence.
Sends transcript + key frames to Claude and returns structured legal summary.
"""

import os
import base64
import logging
import asyncio
from pathlib import Path
from typing import List
import aiohttp

log = logging.getLogger("analyzer")

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-opus-4-5"   # Best reasoning for legal analysis
MAX_TOKENS = 4000
MAX_FRAMES_TO_CLAUDE = 12          # Keep within context + cost limits

# ── Legal Analysis System Prompt ──────────────────────────────────────────────
SYSTEM_PROMPT = """You are a criminal defense paralegal analyst for L & L Law Group, PLLC, 
a criminal defense firm in the Dallas-Fort Worth area. You specialize in analyzing 
body camera footage and in-car (dashcam) video evidence for defense purposes.

Your job is to produce a thorough, organized analysis of video evidence that helps 
defense attorneys and staff quickly understand what happened, identify favorable facts 
for the defense, spot procedural issues, and prepare for court.

Always analyze from the DEFENSE perspective. Note anything that:
- Contradicts the officer's report or narrative
- Supports suppression of evidence (illegal stop, search without consent/warrant)
- Demonstrates lack of probable cause
- Shows client cooperation or non-threatening behavior
- Reveals inconsistencies in officer conduct
- Indicates Miranda rights were not properly given
- Suggests use of excessive force

Be factual and precise. Use timestamps from the transcript when available.
Format your analysis in clear sections as instructed."""


def build_analysis_prompt(
    file_name: str,
    transcript: str,
    duration_seconds: float,
    num_frames: int
) -> str:
    duration_str = _format_duration(duration_seconds)
    video_type = _detect_video_type(file_name)

    return f"""Analyze the following {video_type} evidence for L & L Law Group.

FILE: {file_name}
VIDEO TYPE: {video_type}
DURATION: {duration_str}
FRAMES CAPTURED: {num_frames} key frames provided

---
AUDIO TRANSCRIPT:
{transcript if transcript else '[No audio transcript available — silent video or audio extraction failed]'}
---

{num_frames} key frames from the video are attached as images (chronological order, evenly spaced throughout the video).

Please produce a complete legal analysis in the following format:

═══════════════════════════════════════════════════
CASE VIDEO ANALYSIS — L & L LAW GROUP
FILE: {file_name}
═══════════════════════════════════════════════════

1. INCIDENT OVERVIEW
   - Date/time indicators (from video metadata, timestamps, or context clues)
   - Location (jurisdiction, street, business, etc. — from visual or audio cues)
   - Type of incident (traffic stop, DWI, assault, arrest, etc.)
   - Agencies/officers involved (badge numbers, unit numbers if visible/spoken)
   - Subjects/parties identified (descriptions, names if stated)

2. CHRONOLOGICAL EVENT TIMELINE
   List key events with timestamps (MM:SS) from the transcript or estimated from frames.
   Be specific — note exact commands given, responses made, actions taken.

3. STOP & DETENTION ANALYSIS
   - What was the stated reason for the stop or contact?
   - Was reasonable suspicion/probable cause articulated?
   - At what point was the subject detained (not free to leave)?
   - Was the detention extended beyond the original purpose? If so, why?

4. SEARCH & SEIZURE ISSUES
   - Was any search conducted? (person, vehicle, property)
   - Was consent requested? Given? Voluntarily?
   - Was a warrant mentioned?
   - Any inventory search?
   - Anything seized? What and when?

5. MIRANDA & STATEMENTS
   - Were Miranda rights given? When? Verbatim if possible.
   - Did the subject invoke rights at any point?
   - What statements did the subject make — before and after Miranda?
   - Any potentially suppressible statements?

6. OFFICER CONDUCT FLAGS
   - Professionalism of contact
   - Any use of force? Describe precisely.
   - Threats, coercion, or pressure tactics noted
   - Compliance with department protocols (as observable)
   - Any discrepancies between what is visible/audible and what might be reported

7. DEFENSE FAVORABLE OBSERVATIONS
   List every fact, behavior, or circumstance that could benefit the defense:
   - Client's demeanor and cooperation level
   - Inconsistencies or contradictions
   - Procedural failures
   - Lack of evidence of alleged offense visible on video
   - Officer admissions or statements

8. SUPPRESSION MOTION INDICATORS
   Flag any issues that may support motions to suppress:
   [ ] Unlawful stop (no reasonable suspicion)
   [ ] Unlawful detention (extended without basis)
   [ ] Search without consent or warrant
   [ ] Miranda violation
   [ ] Coerced confession/statement
   [ ] Chain of custody issues
   [ ] Other: ___

9. GAPS & VIDEO QUALITY NOTES
   - Any periods where video is missing, cut, or camera is obscured
   - Audio quality issues affecting reliability of transcript
   - Lighting or angle limitations on visual analysis
   - Anything that could not be confirmed from the footage

10. RECOMMENDED FOLLOW-UP
    Specific actions for the attorney or paralegal:
    - Discovery requests (other camera angles, dispatch audio, etc.)
    - Witness identification
    - Expert needs (accident reconstruction, use-of-force expert, etc.)
    - Immediate legal issues requiring attorney attention

═══════════════════════════════════════════════════
END OF ANALYSIS
Generated by L & L Law Group Case Video Analyzer
═══════════════════════════════════════════════════
"""


class VideoAnalyzer:

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")
        if not self.api_key:
            log.warning("ANTHROPIC_API_KEY not set")

    async def analyze(
        self,
        file_name: str,
        transcript: str,
        frame_paths: List[str],
        duration_seconds: float
    ) -> str:
        """
        Send transcript + frames to Claude and return the legal analysis.
        """
        if not self.api_key:
            return "[Analysis skipped — ANTHROPIC_API_KEY not configured]"

        # Limit frames sent to Claude
        frames_to_send = frame_paths[:MAX_FRAMES_TO_CLAUDE]
        prompt = build_analysis_prompt(
            file_name, transcript, duration_seconds, len(frames_to_send)
        )

        # Build multimodal message content
        content = []

        # Add frames as images
        for frame_path in frames_to_send:
            img_b64 = _encode_image(frame_path)
            if img_b64:
                content.append({
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": img_b64
                    }
                })

        # Add the analysis prompt text
        content.append({"type": "text", "text": prompt})

        payload = {
            "model": CLAUDE_MODEL,
            "max_tokens": MAX_TOKENS,
            "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": content}]
        }

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        log.info(
            f"Calling Claude with {len(frames_to_send)} frames + "
            f"{len(transcript)} char transcript..."
        )

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    ANTHROPIC_API_URL,
                    json=payload,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=300)
                ) as resp:
                    if resp.status != 200:
                        body = await resp.text()
                        log.error(f"Claude API error {resp.status}: {body[:500]}")
                        return f"[Analysis failed — Claude API returned {resp.status}]"

                    data = await resp.json()
                    text_blocks = [
                        b["text"] for b in data.get("content", [])
                        if b.get("type") == "text"
                    ]
                    return "\n".join(text_blocks)

        except asyncio.TimeoutError:
            return "[Analysis timed out — video may be unusually complex]"
        except Exception as e:
            log.error(f"Claude API call failed: {e}", exc_info=True)
            return f"[Analysis error: {str(e)}]"


# ── Helpers ───────────────────────────────────────────────────────────────────
def _encode_image(path: str) -> str:
    """Base64-encode a JPEG frame for the Claude API."""
    try:
        with open(path, "rb") as f:
            return base64.standard_b64encode(f.read()).decode("utf-8")
    except Exception as e:
        log.warning(f"Could not encode frame {path}: {e}")
        return ""


def _detect_video_type(file_name: str) -> str:
    name_lower = file_name.lower()
    if any(kw in name_lower for kw in ["body", "bwc", "bodycam", "body-cam"]):
        return "Body Camera Footage"
    if any(kw in name_lower for kw in ["dash", "incar", "in-car", "mvr", "patrol"]):
        return "In-Car (Dashcam) Footage"
    if any(kw in name_lower for kw in ["surveillance", "cctv", "security"]):
        return "Surveillance / CCTV Footage"
    if any(kw in name_lower for kw in ["cell", "phone", "bystander", "witness"]):
        return "Bystander / Cell Phone Footage"
    return "Law Enforcement Video Evidence"


def _format_duration(seconds: float) -> str:
    if seconds <= 0:
        return "Unknown"
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m {secs}s"
    return f"{minutes}m {secs}s"
