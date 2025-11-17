from working import convert
import pytest

def test_valid_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:15 PM to 3:45 AM") == "13:15 to 03:45"

def test_valid_short_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM-5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # invalid minute
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")  # invalid hour

def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:01 AM to 12:01 PM") == "00:01 to 12:01"
