# test_fixtures.py
import pytest


@pytest.fixture
def user_data():
    data = {
        "username": "Allison",
        "password": "test1234",
        "role": "Tester"
    }
    return data


@pytest.fixture
def browser():
    # Setup
    print("\n🌐 Opening Chrome browser...")
    browser_info = {"name": "Chrome", "is_open": True}

    yield browser_info

    # Teardown
    print("\n🔴 Closing Chrome browser...")
    browser_info["is_open"] = False


# Using user_data fixture
def test_username(user_data):
    assert user_data["username"] == "Allison"

def test_password_length(user_data):
    assert len(user_data["password"]) >= 8

def test_role(user_data):
    assert user_data["role"] == "Tester"


# Using browser fixture
def test_browser_opens(browser):
    assert browser["is_open"] == True

def test_browser_name(browser):
    assert browser["name"] == "Chrome"