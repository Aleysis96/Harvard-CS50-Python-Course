from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
