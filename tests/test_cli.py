import contextlib
import io
import json
import unittest
from new_ai.__main__ import main


class CLITest(unittest.TestCase):
    def test_status_does_not_claim_model_completion(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["status"]), 0)
        record = json.loads(out.getvalue())
        self.assertEqual(record["integrated_model"], "NOT DELIVERED")
        self.assertEqual(record["e20_language"], "NOT RUN")
        self.assertEqual(record["e21_language"], "NOT RUN")

    def test_unavailable_model_command_is_not_simulated(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            main(["prototype"])
        self.assertEqual(raised.exception.code, 2)
