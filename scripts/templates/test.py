import sys
import io
import unittest
import json
import os
import main


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()


class MainTestCase(unittest.TestCase):
    def test_json(self):
        path = (
            os.path.dirname(__file__) + "/case.json"
            if os.path.dirname(__file__)
            else "case.json"
        )
        with open(path) as f:
            data = json.load(f)
            for i, d in enumerate(data):
                with self.subTest(f"case-{i + 1}: {json.dumps(d[0])}"):
                    stub_stdin(self, d[0])
                    stub_stdouts(self)
                    main.main()
                    self.assertEqual(sys.stdout.getvalue(), d[1])


if __name__ == "__main__":
    unittest.main()
