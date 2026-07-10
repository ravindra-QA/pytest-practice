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


@pytest.fixture
def base_config():
    return {
        "base_url": "https://stumbleguys.com",
        "timeout": 30,
        "environment": "Staging"
    }


@pytest.fixture
def test_user():
    return {
        "username": "Allison",
        "password": "test1234",
        "role": "Tester"
    }

@pytest.fixture
def browser_session():
    print("🌐 Browser opened!")
    data = {
        "browser": "Chrome", 
        "is_open": True, 
        "url": ""
    }
    yield data
    print("🔴 Browser closed!")