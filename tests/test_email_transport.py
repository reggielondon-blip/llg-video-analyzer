import io
import json
import unittest
from unittest.mock import patch, MagicMock
from app.email_transport import ZapierEmailTransport, NotificationError
from app import email_notifier


class Response(io.BytesIO):
    def __init__(self, value, sse=False):
        raw=json.dumps(value)
        if sse: raw='event: message\ndata: '+raw+'\n\n'
        super().__init__(raw.encode())
        self.headers={'Mcp-Session-Id':'test-session'}


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.calls=[]
        self.account={'id':'verified-connection','title':'sender@example.invalid','is_stale':'false'}
        self.send_result={'results':[{'id':'test-message-id','threadId':'test-thread'}]}
        self.tool_error=False
        self.sse=False
        self.timeout=False
        self.actions=[{'actions':[{'key':'message','tool_name':'gmail_send_email'}]}]

    def open(self, request, timeout):
        body=json.loads(request.data);self.calls.append(body)
        if self.timeout: raise TimeoutError('SECRET-MCP-URL')
        if body['method']=='initialize':
            return Response({'jsonrpc':'2.0','id':body['id'],'result':{}})
        name=body['params']['name']
        if name=='list_zapier_connections': result={'connections':[self.account]}
        elif name=='inspect_zapier_actions': result=self.actions
        elif name=='execute_zapier_write_action':result=self.send_result
        else: raise AssertionError(name)
        return Response({'jsonrpc':'2.0','id':body['id'],'result':{'isError':self.tool_error,
                         'content':[{'type':'text','text':json.dumps(result)}]}},self.sse)

    def transport(self):
        return ZapierEmailTransport('https://example.invalid/secret','verified-connection',
                                   'sender@example.invalid','recipient@example.invalid',opener=self.open)

    def writes(self):
        return [c for c in self.calls if c.get('params',{}).get('name')=='execute_zapier_write_action']

    def test_sends_only_to_explicit_recipient_and_connection(self):
        self.assertEqual(self.transport().send('subject','body'),'test-message-id')
        self.assertEqual(len(self.writes()),1)
        args=self.writes()[0]['params']['arguments']
        self.assertEqual(args['connection_id'],'verified-connection')
        self.assertEqual(args['params']['to'],['recipient@example.invalid'])
        self.assertNotIn('cc',args['params']);self.assertNotIn('bcc',args['params'])
        self.assertFalse(args['params']['send_to_groups'])

    def test_sse_supported(self):
        self.sse=True
        self.assertEqual(self.transport().send('subject','body'),'test-message-id')

    def test_wrong_account_never_sends(self):
        self.account['title']='wrong@example.invalid'
        with self.assertRaisesRegex(NotificationError,'does not match'):self.transport().send('subject','body')
        self.assertFalse(self.writes())

    def test_missing_connection_never_sends(self):
        self.account['id']='another-connection'
        with self.assertRaises(NotificationError):self.transport().send('subject','body')
        self.assertFalse(self.writes())

    def test_expired_connection_never_sends(self):
        self.account['is_expired']=True
        with self.assertRaises(NotificationError):self.transport().send('subject','body')
        self.assertFalse(self.writes())

    def test_action_schema_mismatch_never_sends(self):
        self.actions=[]
        with self.assertRaises(NotificationError):self.transport().send('subject','body')
        self.assertFalse(self.writes())

    def test_provider_error_not_reported_as_success(self):
        self.tool_error=True
        with self.assertRaises(NotificationError):self.transport().send('subject','body')

    def test_no_receipt_is_uncertain_not_retried(self):
        self.send_result={'results':[]}
        with self.assertRaisesRegex(NotificationError,'delivery uncertain'):self.transport().send('subject','body')
        self.assertEqual(len(self.writes()),1)

    def test_transport_failure_redacts_secret_and_does_not_retry(self):
        self.timeout=True
        with self.assertRaises(NotificationError) as caught:self.transport().send('subject','body')
        self.assertNotIn('SECRET',str(caught.exception))
        self.assertEqual(len(self.calls),1)

    def test_subject_injection_rejected(self):
        with self.assertRaises(NotificationError):self.transport().send('subject\r\nBcc: x','body')
        self.assertFalse(self.calls)

    def test_multiple_recipient_config_rejected(self):
        with self.assertRaises(NotificationError):
            ZapierEmailTransport('https://example.invalid','connection','s@example.invalid','a@example.invalid,b@example.invalid')

    def test_no_smtp_fallback_when_https_fails(self):
        with patch.multiple(email_notifier,TRANSPORT='zapier',ZAPIER_URL='https://example.invalid',
                            ZAPIER_CONNECTION='test',FROM_EMAIL='s@example.invalid',TO_EMAIL='r@example.invalid'), \
             patch('app.email_notifier.ZapierEmailTransport') as transport, \
             patch('app.email_notifier.smtplib.SMTP_SSL') as smtp:
            transport.return_value.send.side_effect=NotificationError('not retried')
            self.assertIsNone(email_notifier._send('subject','body'))
            smtp.assert_not_called()


if __name__=='__main__':
    unittest.main(verbosity=2)
