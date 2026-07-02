# test_conftest_demo.py
# Notice — NO imports needed for fixtures! conftest.py shares them automatically!

def test_username(user_credentials):
    assert user_credentials["username"] == "Allison"

def test_password(user_credentials):
    assert len(user_credentials["password"]) >= 8

def test_base_url(api_config):
    assert api_config["base_url"] == "https://stumbleguys.com"

def test_timeout(api_config):
    assert api_config["timeout"] == 30

def test_environments(test_environments):
    assert "Staging" in test_environments
    assert len(test_environments) == 3