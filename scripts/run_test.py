import sys
import io
import unittest
import json
import os
import fire


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
    TASK_NUMBER = 116

    def test_main(self):
        case_path = f"{os.path.dirname(__file__)}/../tasks/{self.TASK_NUMBER}/case.json"
        main_path = f"{os.path.dirname(__file__)}/../tasks/{self.TASK_NUMBER}/main.py"

        with open(case_path) as f:
            case_data = json.load(f)

        with open(main_path) as f:
            main_text = f.read()

        for i, d in enumerate(case_data):
            with self.subTest(f"case-{i + 1}: {json.dumps(d[0])}"):
                stub_stdin(self, d[0])
                stub_stdouts(self)
                exec(main_text)
                self.assertEqual(sys.stdout.getvalue(), d[1])


def run_test(task_number: int):
    MainTestCase.TASK_NUMBER = task_number
    unittest.main(argv=['first-arg-is-ignored'])


if __name__ == "__main__":
    fire.Fire(run_test)
