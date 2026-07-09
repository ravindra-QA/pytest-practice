# Create another new file test_user_validation.py     New file!

import pytest

# In test_user_validation.py — write test_username_not_empty using test_user fixture — checks username is not emptyassert test_user["username"] != ""
def test_username_not_empty(test_user):
    assert test_user["username"] != ""

# Write test_password_length — checks password length is greater than or equal to 8 len(test_user["password"])
def test_password_length(test_user):
    assert len(test_user["password"]) >= 8

# Write test_user_role — checks role is "Tester"    Mark as regression
@pytest.mark.regression
def test_user_role(test_user):
    assert test_user["role"] == "Tester"

# Run ALL tests together: python -m pytest test_environment.py test_user_validation.py -v
PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_environment.py test_user_validation.py -v
======================================================================== test session starts =========================================================================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\GS02494\Desktop\pytest-practice
configfile: pytest.ini
collected 6 items                                                                                                                                                     

test_environment.py::test_base_url PASSED                                                                                                                       [ 16%]
test_environment.py::test_timeout PASSED                                                                                                                        [ 33%]
test_environment.py::test_environment_is_staging PASSED                                                                                                         [ 50%]
test_user_validation.py::test_username_not_empty PASSED                                                                                                         [ 66%]
test_user_validation.py::test_password_length PASSED                                                                                                            [ 83%]
test_user_validation.py::test_user_role PASSED                                                                                                                  [100%]

========================================================================= 6 passed in 0.13s ==========================================================================

# Run only smoke: python -m pytest test_environment.py test_user_validation.py -m smoke -v Only smoke tests!
PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_environment.py test_user_validation.py -m smoke -v
======================================================================== test session starts =========================================================================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\GS02494\Desktop\pytest-practice
configfile: pytest.ini
collected 6 items / 5 deselected / 1 selected                                                                                                                         

test_environment.py::test_timeout PASSED                                                                                                                        [100%]

================================================================== 1 passed, 5 deselected in 0.10s ===================================================================

# Push ALL new files to GitHubgit add . then commit and push
