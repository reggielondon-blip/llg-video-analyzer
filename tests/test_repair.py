import asyncio
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from app.video_processor import VideoProcessor
from app.drive_client import DriveClient
from app.transcriber import Transcriber
from app.analyzer import VideoAnalyzer
from app import main


class MediaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.video = cls.root / 'sample.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                        'testsrc2=size=160x120:rate=10', '-f', 'lavfi', '-i',
                        'sine=frequency=440:sample_rate=16000', '-t', '2',
                        '-c:v', 'libx264', '-c:a', 'aac', str(cls.video)], check=True)
        cls.silent = cls.root / 'silent.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-i', str(cls.video), '-an',
                        '-c:v', 'copy', str(cls.silent)], check=True)
        cls.corrupt = cls.root / 'truncated.mp4'
        data = cls.video.read_bytes()
        moov = data.find(b'moov')
        assert moov > 4
        cls.corrupt.write_bytes(data[:moov-4])

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def extract(self, path):
        with tempfile.TemporaryDirectory() as out:
            audio, frames, duration = VideoProcessor().extract(str(path), out)
            return bool(audio and Path(audio).stat().st_size), len(frames), duration

    def test_real_short_video_audio_and_frame(self):
        audio, frames, duration = self.extract(self.video)
        self.assertTrue(audio)
        self.assertGreater(frames, 0)
        self.assertAlmostEqual(duration, 2, places=1)

    def test_real_silent_video(self):
        audio, frames, duration = self.extract(self.silent)
        self.assertFalse(audio)
        self.assertGreater(frames, 0)

    def test_corrupt_mp4_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unreadable video'):
            self.extract(self.corrupt)

    def test_audio_extraction_failure_rejected(self):
        with patch.object(VideoProcessor, '_extract_audio', return_value=None):
            with self.assertRaisesRegex(RuntimeError, 'Audio extraction failed'):
                self.extract(self.video)

    def test_frame_extraction_failure_rejected(self):
        with patch.object(VideoProcessor, '_extract_frames', return_value=[]):
            with self.assertRaisesRegex(RuntimeError, 'No video frames'):
                self.extract(self.video)


class DownloadTests(unittest.TestCase):
    def test_integrity(self):
        for size, checksum, expected in [(3, hashlib.md5(b'abc').hexdigest(), False),
                                         (4, hashlib.md5(b'abc').hexdigest(), True),
                                         (3, '0'*32, True)]:
            with self.subTest(size=size, checksum=checksum):
                client = DriveClient.__new__(DriveClient)
                client.service = MagicMock()
                client.get_file_info = MagicMock(return_value={'size': str(size), 'md5Checksum': checksum})
                def downloader(handle, request, **kwargs):
                    handle.write(b'abc')
                    result = MagicMock()
                    result.next_chunk.return_value = (None, True)
                    return result
                with tempfile.TemporaryDirectory() as out, patch('app.drive_client.MediaIoBaseDownload', downloader):
                    if expected:
                        with self.assertRaises(ValueError):
                            client.download_file('file', str(Path(out)/'video'))
                    else:
                        client.download_file('file', str(Path(out)/'video'))


class TranscriptTests(unittest.TestCase):
    def test_failed_states_raise(self):
        transcriber = Transcriber()
        for status in ['timeout', 'error', 'queued', 'unknown']:
            with self.subTest(status=status), self.assertRaises(RuntimeError):
                transcriber._format_transcript({'status': status})

    def test_completed_speech_and_silence(self):
        transcriber = Transcriber()
        self.assertEqual(transcriber._format_transcript({'status':'completed','text':'hello'}), 'hello')
        self.assertEqual(transcriber._format_transcript({'status':'completed','text':None}), '')


class PipelineTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        main.processing_lock = asyncio.Lock()
        self.tmp = tempfile.TemporaryDirectory()
        self.audio = Path(self.tmp.name)/'audio.wav'
        self.audio.write_bytes(b'test fixture, never uploaded')
        self.drive = MagicMock()
        self.drive.get_file_info.return_value = {'name':'sample.mp4','mimeType':'video/mp4'}
        self.drive.upload_analysis.return_value = 'https://example.invalid/test-only'
        self.processor = MagicMock()
        self.processor.extract.return_value = (str(self.audio), ['test-frame'], 2)
        self.transcriber = MagicMock(transcribe=AsyncMock(return_value='Test-only transcript'))
        self.analyzer = MagicMock(analyze=AsyncMock(return_value='Test-only analysis'))
        self.notifier = MagicMock(post_analysis_complete=AsyncMock(), post_error=AsyncMock())
        self.patches = [patch.object(main, k, v) for k,v in {
            'drive_client':self.drive, 'processor':self.processor, 'transcriber':self.transcriber,
            'analyzer':self.analyzer, 'notifier':self.notifier}.items()]
        for p in self.patches: p.start()

    async def asyncTearDown(self):
        for p in reversed(self.patches): p.stop()
        self.tmp.cleanup()

    async def test_valid_pipeline_saves_then_marks(self):
        await main.process_video_file('test')
        self.drive.upload_analysis.assert_called_once()
        self.drive.mark_as_processed.assert_called_once_with('test')
        self.notifier.post_error.assert_not_called()

    async def test_corrupt_input_never_calls_paid_apis_or_saves(self):
        self.processor.extract.side_effect = ValueError('moov atom not found')
        await main.process_video_file('test')
        self.transcriber.transcribe.assert_not_called()
        self.analyzer.analyze.assert_not_called()
        self.drive.upload_analysis.assert_not_called()
        self.drive.mark_as_processed.assert_not_called()
        self.notifier.post_error.assert_awaited_once()

    async def test_transcription_failure_never_analyzes_or_saves(self):
        self.transcriber.transcribe.side_effect = RuntimeError('transcription failed')
        await main.process_video_file('test')
        self.analyzer.analyze.assert_not_called()
        self.drive.upload_analysis.assert_not_called()
        self.drive.mark_as_processed.assert_not_called()

    async def test_analysis_failure_never_saves_or_marks(self):
        self.analyzer.analyze.side_effect = RuntimeError('API failure')
        await main.process_video_file('test')
        self.drive.upload_analysis.assert_not_called()
        self.drive.mark_as_processed.assert_not_called()

    async def test_save_failure_never_marks(self):
        self.drive.upload_analysis.side_effect = RuntimeError('Drive failure')
        await main.process_video_file('test')
        self.drive.mark_as_processed.assert_not_called()

    async def test_previously_processed_skipped(self):
        self.drive.get_file_info.return_value['appProperties'] = {'llg_analyzed':'true'}
        await main.process_video_file('test')
        self.drive.download_file.assert_not_called()

    async def test_slow_download_does_not_block_health(self):
        self.drive.download_file.side_effect = lambda *args: time.sleep(0.3)
        task = asyncio.create_task(main.process_video_file('test'))
        await asyncio.sleep(0.05)
        self.assertFalse(task.done())
        self.assertEqual((await asyncio.wait_for(main.health(), 0.1))['status'], 'ok')
        await task

    async def test_duplicate_requests_serialize_and_skip(self):
        def mark(fid):
            self.drive.get_file_info.return_value['appProperties']={'llg_analyzed':'true'}
        self.drive.mark_as_processed.side_effect = mark
        await asyncio.gather(main.process_video_file('test'), main.process_video_file('test'))
        self.drive.upload_analysis.assert_called_once()


class AnalyzerTests(unittest.IsolatedAsyncioTestCase):
    async def test_missing_key_raises(self):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY':''}):
            with self.assertRaises(RuntimeError):
                await VideoAnalyzer().analyze('test', 'text', [], 2)

    async def test_empty_inputs_rejected(self):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY':'test-not-a-key'}):
            with self.assertRaises(ValueError):
                await VideoAnalyzer().analyze('test', '', [], 2)

    async def test_api_failure_empty_truncation_and_sampling(self):
        for status, content, stop, fails in [(401, [], 'end_turn', True),
                    (200, [], 'end_turn', True),
                    (200, [{'type':'text','text':'partial'}], 'max_tokens', True),
                    (200, [{'type':'text','text':'complete'}], 'end_turn', False)]:
            with self.subTest(status=status,stop=stop,content=content):
                response = MagicMock(status=status)
                response.text = AsyncMock(return_value='test error')
                response.json = AsyncMock(return_value={'content':content,'stop_reason':stop})
                session = MagicMock()
                session.post.return_value.__aenter__ = AsyncMock(return_value=response)
                manager = MagicMock()
                manager.__aenter__ = AsyncMock(return_value=session)
                with patch('app.analyzer.aiohttp.ClientSession', return_value=manager), \
                     patch('app.analyzer._encode_image', side_effect=lambda p: 'encoded-'+p), \
                     patch.dict(os.environ, {'ANTHROPIC_API_KEY':'test-not-a-key'}):
                    call = VideoAnalyzer().analyze('test', 'transcript', [str(i) for i in range(20)], 200)
                    if fails:
                        with self.assertRaises(RuntimeError): await call
                    else:
                        self.assertEqual(await call, 'complete')
                        images = session.post.call_args.kwargs['json']['messages'][0]['content'][:-1]
                        self.assertEqual(len(images), 12)
                        self.assertEqual(images[0]['source']['data'], 'encoded-0')
                        self.assertEqual(images[-1]['source']['data'], 'encoded-19')


if __name__ == '__main__':
    unittest.main(verbosity=2)
