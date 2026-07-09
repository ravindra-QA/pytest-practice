# 1Create test_login_api.py in pytest-practice folderAlready done!

# 2Add import pytest at topAlways first line!
import pytest

# 3Write a fixture called login_response that returns the API response dictionary aboveUse @pytest.fixture
@pytest.fixture
def login_response():
    return {
        "status": 200,
        "message": "Login Successful",
        "user": {
            "id": 101,
            "username": "Allison",
            "role": "Tester"
        }
    }

# 4Write test_status_code — checks status is 200assert response["status"] == 200
def test_status_code(login_response):
    assert login_response["status"] == 200

# 5Write test_message — checks message is "Login Successful"Access dict key
def test_message(login_response):
    assert login_response["message"] == "Login Successful"

# 6Write test_username — checks user["username"] is "Allison"Nested dictionary!
def test_username(login_response):
    assert login_response["user"]["username"] == "Allison"

# 7Write test_user_role — checks user["role"] is "Tester"Same as above
def test_user_role(login_response):
    assert login_response["user"]["role"] == "Tester"

# 8Write test_user_id — checks user["id"] is greater than 0Use > operator
def test_user_id(login_response):
    assert login_response["user"]["id"] > 0

# 9Mark test_status_code and test_message as smoke@pytest.mark.smoke
@pytest.mark.smoke
def test_status_code(login_response):
    assert login_response["status"] == 200

@pytest.mark.smoke
def test_message(login_response):
    assert login_response["message"] == "Login Successful"

# 10Mark test_username, test_user_role, test_user_id as regression@pytest.mark.regression
@pytest.mark.regression
def test_username(login_response):
    assert login_response["user"]["username"] == "Allison"

@pytest.mark.regression
def test_user_role(login_response):
    assert login_response["user"]["role"] == "Tester"

@pytest.mark.regression
def test_user_id(login_response):
    assert login_response["user"]["id"] > 0

# 11Run python -m pytest test_login_api.py -vCheck all pass!


# 12Run python -m pytest test_login_api.py -m smoke -vOnly smoke tests run!

# 13Run python -m pytest test_login_api.py -m regression -vOnly regression tests run!

# 14Push to GitHubgit add, git commit, git push