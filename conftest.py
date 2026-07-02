# conftest.py
import pytest


@pytest.fixture
def user_credentials():
    return {
        "username": "Allison",
        "password": "test1234",
        "role": "Tester"
    }


@pytest.fixture
def api_config():
    return {
        "base_url": "https://stumbleguys.com",
        "timeout": 30,
        "headers": {"Content-Type": "application/json"}
    }


@pytest.fixture
def test_environments():
    return ["Production", "Staging", "Test"]