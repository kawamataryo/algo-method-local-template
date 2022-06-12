import pytest
import fire
import os
import json


def run_test(problem_number: int):
    case_path = f"{os.path.dirname(__file__)}/../../questions/{problem_number}/case.json"
    main_path = f"{os.path.dirname(__file__)}/../../questions/{problem_number}/main.py"

    with open(case_path) as f:
        cases = json.load(f)

    with open(main_path) as f:
        main_text = f.read()

    pytest.main([f"{os.path.dirname(__file__)}/test_main.py", "--no-header",
                "--tb=short", "--disable-warnings", "--cases", json.dumps(cases), "--main", main_text])


if __name__ == "__main__":
    fire.Fire(run_test)
