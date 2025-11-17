from fuel import convert, gauge
import pytest

def test_convert_returns_correct_ints():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99

def test_convert_raises_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("1/")  # Falta denominador

def test_convert_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_labels_empty():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"

def test_gauge_does_not_print_1_percent():
    assert gauge(1) != "1%"
    assert gauge(1) == "E"

def test_gauge_labels_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
