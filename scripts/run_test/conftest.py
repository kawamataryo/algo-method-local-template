import pytest
import json


def pytest_addoption(parser):
    parser.addoption("--cases", action="store", default="[]")
    parser.addoption("--main", action="store", default="print('hello world')")


@pytest.fixture(scope="session")
def cases(pytestconfig):
    return json.loads(pytestconfig.getoption("cases"))


@pytest.fixture(scope="session")
def main(pytestconfig):
    return pytestconfig.getoption("main")
