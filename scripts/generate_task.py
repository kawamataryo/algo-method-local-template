import httpx
from typing import List, Tuple
import re
import os
import shutil
import json
import fire


def extract_io_list_from_text(text: str) -> List[Tuple[str, str]]:
    input_pattern = r"####.*?入力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    input_results = [re.sub(r"\s*?\r", "", r) for r in re.findall(input_pattern, text)]

    output_pattern = r"####.*?出力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    output_results = [
        re.sub(r"\s*?\r", "", r) for r in re.findall(output_pattern, text)
    ]

    if len(input_results) < 1 or len(input_results) != len(output_results):
        raise Exception("Failed to extract input/output from text")
    return [
        (input_result, output_results[i])
        for i, input_result in enumerate(input_results)
    ]


def extract_problem_from_text(text: str) -> str:
    problem_pattern = r"(### ?問題文?[\s\S]*?)### 入出力例"
    problem_result = re.search(problem_pattern, text)

    if problem_result is None:
        raise Exception("Failed to extract problem from text")

    return re.sub(r"\s*?\r", "", problem_result.group(1))


def generate_task(task_number: int) -> None:
    dir_name = f"tasks/{str(task_number)}"

    # fetch task text
    r = httpx.get(
        f"https://algo-method.com/_next/data/ZURzraP6sS_ySnYKIk84m/tasks/{str(task_number)}.json?id={str(task_number)}"
    )
    body_text = r.json()["pageProps"]["tasks"]["body"]
    io_list = extract_io_list_from_text(body_text)
    problem_text = extract_problem_from_text(body_text)

    # generate case.json
    os.makedirs(dir_name, exist_ok=True)
    with open(f"{os.path.dirname(__file__)}/../{dir_name}/case.json", "w") as f:
        json.dump(io_list, f, indent=2)

    # generate main.py
    main_text = ""
    with open(f"{os.path.dirname(__file__)}/templates/main.py", "r") as f:
        main_text = f.read()
    with open(f"{os.path.dirname(__file__)}/../{dir_name}/main.py", "w") as f:
        f.write(f'"""\n{problem_text}\n"""\n\n\n{main_text}')

    # copy template files
    shutil.copy(
        f"{os.path.dirname(__file__)}/templates/test.py",
        f"{os.path.dirname(__file__)}/../{dir_name}/test.py",
    )


if __name__ == "__main__":
    fire.Fire(generate_task)
