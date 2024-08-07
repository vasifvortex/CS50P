from numb3rs import validate

def test_val():
    assert validate("255.255.255.0") == True
    assert validate("25.25.25.0") == True
    assert validate("275.255.255.0") == False
    assert validate("cat") == False
    assert validate("140.247.235.144") == True
    assert validate("-1") == False
    assert validate("275.255.255.0.0") == False
    assert validate("275.255.255") == False
    assert validate("25.25.25.0") == True
    assert validate("5") == False
def test_validate_first_byte():
    assert validate("999.1.1.1") == False
    assert validate("1.999.1.1") == False
    assert validate("1.1.999.1") == False
    assert validate("1.1.1.999") == False
    assert validate("1.1.1.1") == True
