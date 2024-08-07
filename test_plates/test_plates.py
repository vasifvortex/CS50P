from plates import is_valid
import pytest

def test_empty():
    with pytest.raises(TypeError):
        is_valid()

def test_letter():
    assert is_valid("CS50P") == False
    assert is_valid("H") == False

def test_number_placement():
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("50") == False

def test_length():
    assert is_valid("12345678") == False
