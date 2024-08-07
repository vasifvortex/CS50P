from working import convert
import pytest
def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
def test_sys_exit():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60")
        assert convert("9 AM - 5 PM")
        assert convert("09:00 AM - 17:00 PM")
        assert convert("8:60 AM to 4:60 PM")
        assert convert("9AM to 5PM")
        assert convert("09:00 to 17:00")
        assert convert("9 AM - 5 PM")
        assert convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        assert convert("9AM - 5PM")
