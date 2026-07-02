# test_classes.py

class TestMath:

    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 10 - 3 == 7

    def test_multiplication(self):
        assert 4 * 4 == 16


class TestStrings:

    def test_uppercase(self):
        assert "allison".upper() == "ALLISON"

    def test_contains(self):
        assert "automation" in "automation testing"

    def test_length(self):
        assert len("pytest") == 6