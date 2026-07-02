# test_basics.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 10 - 5 == 5

def test_multiplication():
    assert 3 * 3 == 9

def test_division():
    assert 10 / 2 == 5.0

def test_that_fails():
    assert 2 + 2 == 5    # this one is WRONG on purpose!