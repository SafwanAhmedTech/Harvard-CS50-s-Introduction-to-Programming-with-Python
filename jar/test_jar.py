from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-3)
        Jar(0)
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(500000)

def test_withdraw():
    jar = Jar()
    Jar(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)
