from working import convert
import pytest
def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_nozero():
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'

def test_incorrect():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert('9:30 AM5:30 PM')
