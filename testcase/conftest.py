import pytest
from loguru import logger


@pytest.fixture(scope="session", autouse=True)
def log():
    print("dasdasd")
