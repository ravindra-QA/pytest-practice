import pytest


@pytest.fixture
def sample_user():
    data = {"name": "Allison", "age": 25, "is_active": True}
    return data

def test_name(sample_user):
    assert sample_user["name"] == "Allison"

def test_age(sample_user):
    assert sample_user["age"] == 25

def test_is_active(sample_user):
    assert sample_user["is_active"] == True

@pytest.mark.parametrize("age", [18, 25, 30, 45, 60])
def test_valid_ages(age):
    assert age in [18, 25, 30, 45, 60]

@pytest.mark.smoke
def test_smoke_check():
    assert True

@pytest.mark.regression
def test_regression_check():
    assert 1 + 1 == 2