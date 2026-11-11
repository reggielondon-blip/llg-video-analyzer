"""Gmail alerts over the existing Zapier HTTPS connection.

Only the configured Gmail account can send to the configured single recipient.
No automatic retries: a timeout after submission can mean delivery is uncertain.
The MCP URL is a secret; never include request URLs or raw exceptions in logs.
"""
import json
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class NotificationError(RuntimeError):
    pass


class ZapierEmailTransport:
    def __init__(self, url, connection_id, sender, recipient, opener=None):
        if not url or urlparse(url).scheme != 'https':
            raise NotificationError('A valid HTTPS Zapier connection is required')
        if not connection_id or not sender or not recipient:
            raise NotificationError('Gmail connection, sender and recipient are required')
        if any(c in sender + recipient for c in '\r\n,;<>'):
            raise NotificationError('Only single plain email addresses are permitted')
        if '@' not in sender or '@' not in recipient:
            raise NotificationError('Invalid notification address')
        self.url = url
        self.connection_id = connection_id
        self.sender = sender
        self.recipient = recipient
        self.opener = opener or urlopen
        self.sid = None
        self.sequence = 0

    def _rpc(self, method, params):
        self.sequence += 1
        payload = {'jsonrpc': '2.0', 'id': self.sequence, 'method': method, 'params': params}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
        if self.sid:
            headers['Mcp-Session-Id'] = self.sid
        request = Request(self.url, data=json.dumps(payload).encode(), headers=headers, method='POST')
        try:
            with self.opener(request, timeout=45) as response:
                self.sid = response.headers.get('Mcp-Session-Id') or self.sid
                raw = response.read().decode('utf-8')
            # The established server may return JSON or SSE-wrapped JSON-RPC.
            if not raw.lstrip().startswith('{'):
                events = [line[5:].strip() for line in raw.splitlines() if line.startswith('data:')]
                raw = events[-1] if events else ''
            result = json.loads(raw)
        except Exception as exc:
            # Do not leak a secret-bearing URL in urllib exception text.
            raise NotificationError('Zapier request failed (' + type(exc).__name__ + '); not retried') from None
        if result.get('error'):
            raise NotificationError('Zapier protocol error; not retried')
        if result.get('id') != self.sequence:
            raise NotificationError('Zapier response identifier mismatch')
        return result.get('result', {})

    def _tool(self, name, arguments):
        result = self._rpc('tools/call', {'name': name, 'arguments': arguments})
        if result.get('isError'):
            raise NotificationError('Zapier Gmail action failed; not retried')
        texts = [part.get('text', '') for part in result.get('content', []) if part.get('type') == 'text']
        if not texts:
            raise NotificationError('Zapier returned no action result; not retried')
        try:
            return json.loads(texts[0])
        except (TypeError, ValueError):
            raise NotificationError('Zapier action result was not JSON; not retried') from None

    def send(self, subject, body):
        if any(c in subject for c in '\r\n'):
            raise NotificationError('Notification subject contains a line break')
        self._rpc('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {},
                                'clientInfo': {'name': 'llg-video-alerts', 'version': '1'}})
        # Re-verify account identity, not the server's default connection.
        accounts = self._tool('list_zapier_connections', {'selected_api': 'GoogleMailV2CLIAPI', 'limit': 100})
        account = next((c for c in accounts.get('connections', [])
                        if str(c.get('id')) == str(self.connection_id)), None)
        if not account or account.get('title', '').strip().lower() != self.sender.lower():
            raise NotificationError('Configured Gmail connection does not match the sender; nothing sent')
        if str(account.get('is_stale', 'false')).lower() == 'true' or str(account.get('is_expired', 'false')).lower() == 'true':
            raise NotificationError('Gmail connection needs reconnection; nothing sent')
        actions = self._tool('inspect_zapier_actions', {
            'selected_api': 'GoogleMailV2CLIAPI', 'tool_name': 'gmail_send_email',
            'connection_id': self.connection_id,
            'params': {'send_to_groups': False},
        })
        if not isinstance(actions, list) or not any(
                a.get('key') == 'message' and a.get('tool_name') == 'gmail_send_email'
                for app in actions for a in app.get('actions', [])):
            raise NotificationError('Expected Gmail send action is unavailable; nothing sent')
        result = self._tool('execute_zapier_write_action', {
            'selected_api': 'GoogleMailV2CLIAPI', 'action': 'message', 'tool_name': 'gmail_send_email',
            'connection_id': self.connection_id,
            'params': {'to': [self.recipient], 'subject': subject, 'body': body,
                       'body_type': 'plain', 'from_name': 'L&L Case Video Analyzer',
                       'send_to_groups': False},
        })
        records = result.get('results', []) if isinstance(result, dict) else result
        if isinstance(result, dict) and result.get('id'):
            records = [result]
        if not isinstance(records, list) or len(records) != 1 or not records[0].get('id'):
            raise NotificationError('Gmail submission has no message receipt; delivery uncertain; not retried')
        return str(records[0]['id'])
