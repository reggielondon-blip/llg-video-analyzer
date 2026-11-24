"""Provider-boundary checks; no paid calls or messages are sent."""
import os
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from app.analyzer import VideoAnalyzer, build_analysis_prompt
from app.transcriber import Transcriber
from app import main


def fake_session(body):
    response = MagicMock(status=200)
    response.json = AsyncMock(return_value=body)
    session = MagicMock()
    session.post.return_value.__aenter__ = AsyncMock(return_value=response)
    manager = MagicMock()
    manager.__aenter__ = AsyncMock(return_value=session)
    return manager, session


class ModelUpgradeTests(unittest.IsolatedAsyncioTestCase):
    async def test_thinking_blocks_are_not_saved_as_report(self):
        manager, session = fake_session({
            'model':'claude-opus-5-5', 'stop_reason':'end_turn',
            'content':[{'type':'thinking','thinking':'private reasoning'},
                       {'type':'text','text':'Complete report.'}],
            'usage':{'input_tokens':300,'output_tokens':500},
        })
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY':'test-only'}), \
             patch('app.analyzer.aiohttp.ClientSession',return_value=manager):
            report = await VideoAnalyzer().analyze('fixture.mp4','A test transcript.',[],34)
        self.assertEqual(report,'Complete report.')
        payload=session.post.call_args.kwargs['json']
        self.assertEqual(payload['model'],'claude-opus-5-5')
        self.assertEqual(payload['output_config'],{'effort':'medium'})
        self.assertEqual(payload['max_tokens'],8192)
        for removed in ['temperature','top_p','top_k','thinking']:
            self.assertNotIn(removed,payload)

    async def test_thinking_only_or_exhausted_budget_cannot_pass(self):
        for content, stop in [([{'type':'thinking','thinking':''}],'end_turn'),
                              ([{'type':'text','text':'unfinished'}],'max_tokens'),
                              ([{'type':'text','text':'refused'}],'refusal')]:
            manager,_=fake_session({'content':content,'stop_reason':stop})
            with self.subTest(stop=stop), \
                 patch.dict(os.environ, {'ANTHROPIC_API_KEY':'test-only'}), \
                 patch('app.analyzer.aiohttp.ClientSession',return_value=manager):
                with self.assertRaises(RuntimeError):
                    await VideoAnalyzer().analyze('fixture.mp4','transcript',[],34)

    async def test_transcript_request_preserves_language_and_evidence_options(self):
        _,session=fake_session({'id':'test-transcript'})
        tid=await Transcriber()._request_transcript(session,'https://example.invalid/test')
        self.assertEqual(tid,'test-transcript')
        p=session.post.call_args.kwargs['json']
        self.assertEqual(p['speech_models'],['assemblyai-stt-3-7','universal-2'])
        self.assertTrue(p['language_detection'])
        self.assertTrue(p['speaker_labels'])
        self.assertFalse(p['filter_profanity'])
        self.assertFalse(p['disfluencies'])
        self.assertIn('Miranda',p['keyterms_prompt'])
        self.assertNotIn('word_boost',p)
        self.assertNotIn('boost_param',p)

    async def test_health_reports_models_without_secrets(self):
        h=await main.health()
        self.assertEqual(h['models']['analysis'],'claude-opus-5-5')
        self.assertEqual(h['models']['transcription'],['assemblyai-stt-3-7','universal-2'])
        self.assertNotIn('key',str(h).lower())

    def test_empty_transcript_does_not_imply_absent_audio(self):
        prompt = build_analysis_prompt('fixture.mp4', '', 35, 4)
        self.assertIn('No speech was transcribed; review the original audio', prompt)
        self.assertIn('It does NOT establish', prompt)
        self.assertIn('Events and motion between frames have not been evaluated.', prompt)
        with_speech = build_analysis_prompt('fixture.mp4', 'Recognized speech.', 35, 4)
        self.assertIn('Recognized speech.', with_speech)
