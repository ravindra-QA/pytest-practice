# test_parametrize.py
import pytest


# Simple parametrize — one parameter
@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_number_is_positive(number):
    assert number > 0


# Multiple values — testing status codes
@pytest.mark.parametrize("status_code", [200, 201, 204])
def test_valid_status_codes(status_code):
    assert status_code in [200, 201, 204]


# Multiple parameters — username AND password
@pytest.mark.parametrize("username, password", [
    ("Allison", "test1234"),
    ("John", "pass5678"),
    ("Sara", "secure99"),
])
def test_login_combinations(username, password):
    assert len(username) > 0
    assert len(password) >= 8


# Parametrize with expected results
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert a + b == expected