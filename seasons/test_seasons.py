import pytest
from seasons import Birthdate
from unittest.mock import patch
from datetime import date

@pytest.fixture
def mock_date(monkeypatch):
    def mock_input(prompt):
        return "2002-11-11"
    monkeypatch.setattr('builtins.input', mock_input)

def test_birthdate_valid(mock_date):
    expected_output = Birthdate(int((date.today() - date(2002,11,11)).total_seconds()/ 60)).__str__()
    birthdate = Birthdate.get()
    print(str(birthdate))
    print(expected_output)
    assert str(birthdate) == expected_output

def test_birthdate_invalid_format(monkeypatch):
    def mock_input(prompt):
        return "hi"
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit) as excinfo:
        Birthdate.get()
    assert str(excinfo.value) == "Format should be ####-##-##"
"""
if __name__ == "__main__":
    pytest.main()
"""
