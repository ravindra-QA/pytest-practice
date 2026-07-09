# # 1Create test_login_api.py in pytest-practice folderAlready done!

# # 2Add import pytest at topAlways first line!
# import pytest

# # 3Write a fixture called login_response that returns the API response dictionary aboveUse @pytest.fixture
# @pytest.fixture
# def login_response():
#     return {
#         "status": 200,
#         "message": "Login Successful",
#         "user": {
#             "id": 101,
#             "username": "Allison",
#             "role": "Tester"
#         }
#     }

# # 4Write test_status_code — checks status is 200assert response["status"] == 200
# def test_status_code(login_response):
#     assert login_response["status"] == 200

# # 5Write test_message — checks message is "Login Successful"Access dict key
# def test_message(login_response):
#     assert login_response["message"] == "Login Successful"

# # 6Write test_username — checks user["username"] is "Allison"Nested dictionary!
# def test_username(login_response):
#     assert login_response["user"]["username"] == "Allison"

# # 7Write test_user_role — checks user["role"] is "Tester"Same as above
# def test_user_role(login_response):
#     assert login_response["user"]["role"] == "Tester"

# # 8Write test_user_id — checks user["id"] is greater than 0Use > operator
# def test_user_id(login_response):
#     assert login_response["user"]["id"] > 0

# # 9Mark test_status_code and test_message as smoke@pytest.mark.smoke
# @pytest.mark.smoke
# def test_status_code(login_response):
#     assert login_response["status"] == 200

# @pytest.mark.smoke
# def test_message(login_response):
#     assert login_response["message"] == "Login Successful"

# # 10Mark test_username, test_user_role, test_user_id as regression@pytest.mark.regression
# @pytest.mark.regression
# def test_username(login_response):
#     assert login_response["user"]["username"] == "Allison"

# @pytest.mark.regression
# def test_user_role(login_response):
#     assert login_response["user"]["role"] == "Tester"

# @pytest.mark.regression
# def test_user_id(login_response):
#     assert login_response["user"]["id"] > 0

# # 11Run python -m pytest test_login_api.py -vCheck all pass!
# PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_login_api.py -v
# ======================================================================== test session starts =========================================================================
# platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\GS02494\Desktop\pytest-practice
# configfile: pytest.ini
# collected 5 items                                                                                                                                                     

# test_login_api.py::test_status_code PASSED                                                                                                                      [ 20%]
# test_login_api.py::test_message PASSED                                                                                                                          [ 40%]
# test_login_api.py::test_username PASSED                                                                                                                         [ 60%]
# test_login_api.py::test_user_role PASSED                                                                                                                        [ 80%]
# test_login_api.py::test_user_id PASSED                                                                                                                          [100%]

# ========================================================================= 5 passed in 0.05s ==========================================================================

# # 12Run python -m pytest test_login_api.py -m smoke -vOnly smoke tests run!
# PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_login_api.py -m smoke -v
# ======================================================================== test session starts =========================================================================
# platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\GS02494\Desktop\pytest-practice
# configfile: pytest.ini
# collected 5 items / 3 deselected / 2 selected                                                                                                                         

# test_login_api.py::test_status_code PASSED                                                                                                                      [ 50%]
# test_login_api.py::test_message PASSED                                                                                                                          [100%]

# ================================================================== 2 passed, 3 deselected in 0.04s ===================================================================

# # 13Run python -m pytest test_login_api.py -m regression -vOnly regression tests run!
# PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_login_api.py -m regression -v
# ======================================================================== test session starts =========================================================================
# platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\GS02494\Desktop\pytest-practice
# configfile: pytest.ini
# collected 5 items / 2 deselected / 3 selected                                                                                                                         

# test_login_api.py::test_username PASSED                                                                                                                         [ 33%]
# test_login_api.py::test_user_role PASSED                                                                                                                        [ 66%]
# test_login_api.py::test_user_id PASSED                                                                                                                          [100%]

# ================================================================== 3 passed, 2 deselected in 0.03s ===================================================================

# # 14Push to GitHubgit add, git commit, git push
# PS C:\Users\GS02494\Desktop\pytest-practice> git add .
# PS C:\Users\GS02494\Desktop\pytest-practice> git commit
# Aborting commit due to empty commit message.
# PS C:\Users\GS02494\Desktop\pytest-practice> git push
# Everything up-to-date


import pytest

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

@pytest.mark.smoke
def test_status_code(login_response):
    assert login_response["status"] == 200

@pytest.mark.smoke
def test_message(login_response):
    assert login_response["message"] == "Login Successful"

@pytest.mark.regression
def test_username(login_response):
    assert login_response["user"]["username"] == "Allison"

@pytest.mark.regression
def test_user_role(login_response):
    assert login_response["user"]["role"] == "Tester"

@pytest.mark.regression
def test_user_id(login_response):
    assert login_response["user"]["id"] > 0



PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_login_api.py -v                         
======================================================================== test session starts =========================================================================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\GS02494\Desktop\pytest-practice
configfile: pytest.ini
collected 5 items                                                                                                                                                     

test_login_api.py::test_status_code PASSED                                                                                                                      [ 20%]
test_login_api.py::test_message PASSED                                                                                                                          [ 40%]
test_login_api.py::test_username PASSED                                                                                                                         [ 60%]
test_login_api.py::test_user_role PASSED                                                                                                                        [ 80%]
test_login_api.py::test_user_id PASSED                                                                                                                          [100%]

========================================================================= 5 passed in 0.04s ==========================================================================
PS C:\Users\GS02494\Desktop\pytest-practice> git add test_login_api.py                                     
PS C:\Users\GS02494\Desktop\pytest-practice> git commit -m "Added login API test with fixtures and markers"
[main 9aae126] Added login API test with fixtures and markers
 1 file changed, 114 insertions(+), 31 deletions(-)
PS C:\Users\GS02494\Desktop\pytest-practice> git push                                                      
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.45 KiB | 740.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ravindra-QA/pytest-practice.git
   313e1c3..9aae126  main -> main