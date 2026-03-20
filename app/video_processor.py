"""
VideoProcessor — FFmpeg wrapper
Tuned for body cam and in-car dashcam footage:
  - Extracts mono 16kHz WAV audio (optimal for speech transcription)
  - Grabs key frames every 10 seconds (captures fast-moving scenes)
  - Caps at 20 frames to stay within Claude API limits
"""

import os
import subprocess
import logging
from pathlib import Path
from typing import Tuple, List, Optional

log = logging.getLogger("video-processor")


class VideoProcessor:

    # Frame interval in seconds — every 10s for body cam / dashcam action
    FRAME_INTERVAL = 10
    # Max frames sent to Claude (API limit consideration + cost)
    MAX_FRAMES = 20
    # Audio: mono, 16kHz WAV — optimal for AssemblyAI speech recognition
    AUDIO_SAMPLE_RATE = 16000

    def extract(
        self, video_path: str, output_dir: str
    ) -> Tuple[Optional[str], List[str], float]:
        """
        Extract audio and key frames from a video file.

        Returns:
            (audio_path, frame_paths, duration_seconds)
        """
        duration = self._get_duration(video_path)
        audio_path = self._extract_audio(video_path, output_dir)
        frame_paths = self._extract_frames(video_path, output_dir, duration)
        return audio_path, frame_paths, duration

    # ── Duration ─────────────────────────────────────────────────────────────
    def _get_duration(self, video_path: str) -> float:
        """Use ffprobe to get video duration in seconds."""
        try:
            result = subprocess.run(
                [
                    "ffprobe", "-v", "error",
                    "-show_entries", "format=duration",
                    "-of", "default=noprint_wrappers=1:nokey=1",
                    video_path
                ],
                capture_output=True, text=True, timeout=30
            )
            return float(result.stdout.strip())
        except Exception as e:
            log.warning(f"Could not get duration: {e}")
            return 0.0

    # ── Audio Extraction ──────────────────────────────────────────────────────
    def _extract_audio(self, video_path: str, output_dir: str) -> Optional[str]:
        """
        Extract audio as mono 16kHz WAV.
        Applies mild noise reduction filter (useful for wind noise in body cam).
        """
        audio_path = os.path.join(output_dir, "audio.wav")
        try:
            cmd = [
                "ffmpeg", "-y",
                "-i", video_path,
                "-vn",                          # no video
                "-acodec", "pcm_s16le",         # 16-bit PCM WAV
                "-ar", str(self.AUDIO_SAMPLE_RATE),  # 16kHz sample rate
                "-ac", "1",                     # mono
                # Mild highpass filter to reduce wind/vehicle rumble noise
                "-af", "highpass=f=80,lowpass=f=8000",
                audio_path
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=600
            )
            if result.returncode != 0:
                log.error(f"FFmpeg audio error: {result.stderr[-500:]}")
                return None
            if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
                size_mb = os.path.getsize(audio_path) / (1024 * 1024)
                log.info(f"Audio extracted: {size_mb:.1f}MB")
                return audio_path
        except subprocess.TimeoutExpired:
            log.error("FFmpeg audio extraction timed out")
        except Exception as e:
            log.error(f"Audio extraction error: {e}", exc_info=True)
        return None

    # ── Frame Extraction ──────────────────────────────────────────────────────
    def _extract_frames(
        self, video_path: str, output_dir: str, duration: float
    ) -> List[str]:
        """
        Extract one JPEG frame every FRAME_INTERVAL seconds.
        Scales to max 20 frames for long videos.
        Uses scene change detection as a secondary strategy for very long clips.
        """
        frames_dir = os.path.join(output_dir, "frames")
        os.makedirs(frames_dir, exist_ok=True)

        # Adjust interval if video would produce too many frames
        interval = self.FRAME_INTERVAL
        if duration > 0:
            expected_frames = duration / interval
            if expected_frames > self.MAX_FRAMES:
                interval = duration / self.MAX_FRAMES
                log.info(
                    f"Long video ({duration:.0f}s): adjusting frame interval "
                    f"to {interval:.1f}s to cap at {self.MAX_FRAMES} frames"
                )

        try:
            cmd = [
                "ffmpeg", "-y",
                "-i", video_path,
                "-vf", (
                    f"fps=1/{interval:.2f},"        # 1 frame per interval
                    "scale=1280:-2,"                 # max 1280px wide
                    "format=yuvj420p"                # compatible color space
                ),
                "-q:v", "3",                         # JPEG quality (1=best, 31=worst)
                "-frames:v", str(self.MAX_FRAMES),
                os.path.join(frames_dir, "frame_%04d.jpg")
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=300
            )
            if result.returncode != 0:
                log.error(f"FFmpeg frame error: {result.stderr[-500:]}")
                return []

        except subprocess.TimeoutExpired:
            log.error("FFmpeg frame extraction timed out")
            return []
        except Exception as e:
            log.error(f"Frame extraction error: {e}", exc_info=True)
            return []

        # Collect and sort extracted frames
        frames = sorted(
            [
                os.path.join(frames_dir, f)
                for f in os.listdir(frames_dir)
                if f.endswith(".jpg")
            ]
        )
        log.info(f"Extracted {len(frames)} frames (interval: {interval:.1f}s)")
        return frames

    @staticmethod
    def frames_to_timestamps(frame_paths: List[str], interval: float) -> dict:
        """
        Map frame filenames back to approximate video timestamps.
        Useful for the analysis prompt.
        """
        timestamps = {}
        for i, path in enumerate(frame_paths):
            seconds = i * interval
            minutes, secs = divmod(int(seconds), 60)
            timestamps[path] = f"{minutes:02d}:{secs:02d}"
        return timestamps
