# test_environment.py


# Create new file test_environment.pyNew file!

import pytest

# In test_environment.py — write test_base_url using base_config fixture — checks url starts with "https"     base_config["base_url"].startswith("https")
def test_base_url(base_config):
    assert base_config["base_url"].startswith("https")

# Write test_timeout — checks timeout is greater than 0
@pytest.mark.smoke
def test_timeout(base_config):
    assert base_config["timeout"] > 0

# Write test_environment_is_staging — checks environment is "Staging"       Mark as regression
@pytest.mark.regression
def test_environment_is_staging(base_config):
    assert base_config["environment"] == "Staging"