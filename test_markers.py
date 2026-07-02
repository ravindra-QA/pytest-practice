# test_markers.py
import pytest


@pytest.mark.smoke
def test_homepage_loads():
    assert True

@pytest.mark.smoke
def test_login_page_loads():
    assert True

@pytest.mark.regression
def test_login_valid_credentials():
    assert "Allison" == "Allison"

@pytest.mark.regression
def test_login_invalid_credentials():
    assert "wrong" != "Allison"

@pytest.mark.api
def test_api_status_code():
    assert 200 == 200

@pytest.mark.api
def test_api_response_message():
    assert "Success" == "Success"

@pytest.mark.smoke
@pytest.mark.regression
def test_logout():
    assert True