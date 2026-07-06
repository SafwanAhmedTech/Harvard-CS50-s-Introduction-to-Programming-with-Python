from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ValueError):
        convert('3/2')
    with pytest.raises(ValueError):
        convert('-3/2')
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(75) =='75%'
