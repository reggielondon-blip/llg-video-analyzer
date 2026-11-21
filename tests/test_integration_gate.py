"""Auth and input-limit checks for optional integration reads."""

import importlib
import os
import unittest

import app.integration_gate as gate


def reload_gate(token):
    if token is None:
        os.environ.pop("INTEGRATIONS_API_TOKEN", None)
    else:
        os.environ["INTEGRATIONS_API_TOKEN"] = token
    return importlib.reload(gate)


class IntegrationGateTests(unittest.TestCase):
    def setUp(self):
        self._original = os.environ.get("INTEGRATIONS_API_TOKEN")

    def tearDown(self):
        if self._original is None:
            os.environ.pop("INTEGRATIONS_API_TOKEN", None)
        else:
            os.environ["INTEGRATIONS_API_TOKEN"] = self._original
        importlib.reload(gate)

    def test_unconfigured_without_token(self):
        mod = reload_gate(None)
        self.assertEqual(mod.auth_status(None), "unconfigured")
        self.assertEqual(mod.auth_status("Bearer anything"), "unconfigured")

    def test_reject_missing_wrong_and_wrong_length_bearer(self):
        mod = reload_gate("correct-token")
        self.assertEqual(mod.auth_status(None), "unauthorized")
        self.assertEqual(mod.auth_status("correct-token"), "unauthorized")
        self.assertEqual(mod.auth_status("Bearer wrong-token"), "unauthorized")
        self.assertEqual(mod.auth_status("Bearer short"), "unauthorized")
        self.assertEqual(mod.auth_status("Bearer correct-token-extra"), "unauthorized")

    def test_accept_exact_bearer(self):
        mod = reload_gate("correct-token")
        self.assertEqual(mod.auth_status("Bearer correct-token"), "ok")

    def test_clamp_int_and_valid_date(self):
        self.assertEqual(gate.clamp_int(50, 1, 90), 50)
        self.assertEqual(gate.clamp_int(0, 1, 90), 1)
        self.assertEqual(gate.clamp_int(200, 1, 100), 100)
        self.assertEqual(gate.clamp_int("nope", 1, 90), 1)
        self.assertEqual(gate.clamp_int(None, 1, 100), 1)
        self.assertTrue(gate.valid_date("2024-01-01"))
        self.assertFalse(gate.valid_date("01-01-2024"))
        self.assertFalse(gate.valid_date("2024/01/01"))
        self.assertFalse(gate.valid_date(""))
        self.assertFalse(gate.valid_date("2024-1-1"))
        self.assertFalse(gate.valid_date(None))


if __name__ == "__main__":
    unittest.main()
