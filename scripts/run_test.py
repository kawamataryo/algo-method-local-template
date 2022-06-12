import pytest
import fire
import os
import json


def run_test(task_number: int):
    global case_data
    global main_text

    case_path = f"{os.path.dirname(__file__)}/../tasks/{task_number}/case.json"
    main_path = f"{os.path.dirname(__file__)}/../tasks/{task_number}/main.py"

    with open(case_path) as f:
        cases = json.load(f)

    with open(main_path) as f:
        main_text = f.read()

    pytest.main([f"{os.path.dirname(__file__)}/tests/test_main.py", "--no-header",
                "--tb=short", "--disable-warnings", "--cases", json.dumps(cases), "--main", main_text])


if __name__ == "__main__":
    fire.Fire(run_test)
