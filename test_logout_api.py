import pytest

@pytest.fixture
def logout_session():
    return {
        "status": 200, 
        "message": "Logged Out Successfully", 
        "session_active": False
    }

@pytest.mark.smoke
def test_browser_is_open(browser_session):
    assert browser_session["is_open"] == True

@pytest.mark.smoke
def test_browser_name(browser_session):
    assert browser_session["browser"] == "Chrome"

@pytest.mark.regression
def test_navigate(browser_session):
    browser_session["url"] = "https://stumbleguys.com"
    assert browser_session["url"].startswith("https")

@pytest.mark.smoke
def test_status(logout_session):
    assert logout_session["status"] == 200

@pytest.mark.regression
def test_logout(logout_session):
    assert logout_session["message"] == "Logged Out Successfully"

@pytest.mark.regression
def test_session(logout_session):
    assert logout_session["session_active"] == False