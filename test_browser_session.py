import pytest

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

@pytest.mark.parametrize("browsers", ["Chrome", "Firefox", "Safari", "Edge"])
def test_supported_browsers(browsers):
    assert isinstance(browsers, str)