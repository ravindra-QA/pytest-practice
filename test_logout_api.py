import pytest

@pytest.fixture
def logout_session():
    return {
        "status": 200,
        "message": "Logged Out Successfully",
        "session_active": False
    }

@pytest.mark.smoke
def test_logout_status(logout_session):
    assert logout_session["status"] == 200

@pytest.mark.smoke
def test_logout_message(logout_session):
    assert logout_session["message"] == "Logged Out Successfully"

@pytest.mark.regression
def test_session_inactive(logout_session):
    assert logout_session["session_active"] == False

@pytest.mark.regression
def test_status_in_valid_codes(logout_session):
    assert logout_session["status"] in [200, 201, 204]