import httpx
from typing import List, Tuple
import re
import os
import json
import fire
from bs4 import BeautifulSoup


def extract_io_list_from_text(text: str) -> List[Tuple[str, str]]:
    input_pattern = r"####.*?入力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    input_results = [re.sub(r"\s*?\r", "", r)
                     for r in re.findall(input_pattern, text)]

    output_pattern = r"####.*?出力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    output_results = [
        re.sub(r"\s*?\r", "", r) for r in re.findall(output_pattern, text)
    ]

    if len(input_results) < 1 or len(input_results) != len(output_results):
        raise Exception("Failed to extract input/output from text")
    return [
        # if output_results is only '\n', result is blank.
        (input_result, output_results[i] if output_results[i] != "\n" else "")
        for i, input_result in enumerate(input_results)
    ]


def extract_problem_from_text(text: str) -> str:
    problem_pattern = r"(### ?問題文?[\s\S]*?)### 入出力例"
    problem_result = re.search(problem_pattern, text)

    if problem_result is None:
        raise Exception("Failed to extract problem from text")

    return re.sub(r"\s*?\r", "", problem_result.group(1))


def fetch_question_body(url: str) -> str:
    res = httpx.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select_one('#__NEXT_DATA__').get_text()
    return json.loads(data)["props"]["pageProps"]["tasks"]["body"]


def get_question(question_number: int) -> None:
    dir_name = f"questions/{str(question_number)}"
    BASE_URL = "https://algo-method.com/tasks"

    body_text = fetch_question_body(f"{BASE_URL}/{question_number}")

    io_list = extract_io_list_from_text(body_text)
    problem_text = extract_problem_from_text(body_text)

    # generate case.json
    os.makedirs(dir_name, exist_ok=True)
    with open(f"{os.path.dirname(__file__)}/../../{dir_name}/case.json", "w") as f:
        json.dump(io_list, f, indent=2)

    # generate main.py
    with open(f"{os.path.dirname(__file__)}/../../{dir_name}/main.py", "w") as f:
        f.write(
            f'"""\n{BASE_URL}/{str(question_number)}\n\n{problem_text}"""\n\nprint("Hello Algor-Method!")\n')


if __name__ == "__main__":
    fire.Fire(get_question)
