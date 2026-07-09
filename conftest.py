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

# Open existing conftest.py in your folderAlready exists!

# Add a new fixture called base_config returning: {"base_url": "https://stumbleguys.com", "timeout": 30, "environment": "Staging"}@pytest.fixture
@pytest.fixture
def base_config():
    return {
        "base_url": "https://stumbleguys.com",
        "timeout": 30,
        "environment": "Staging"
    }


# Add another fixture called test_user returning: {"username": "Allison", "password": "test1234", "role": "Tester"}Same as above
@pytest.fixture
def test_user():
    return {
        "username": "Allison",
        "password": "test1234",
        "role": "Tester"
    }