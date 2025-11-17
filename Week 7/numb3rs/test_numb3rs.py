#  implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly,
# each of whose names should begin with test_

from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.0.1") == "True"
    assert validate("255.255.255.255") == "True"
    assert validate("0.0.0.0") == "True"
    assert validate("127.0.0.1") == "True"

def test_invalid_ips_out_of_range():
    assert validate("256.100.50.25") == "False"
    assert validate("192.168.300.1") == "False"
    assert validate("999.999.999.999") == "False"

def test_invalid_ips_format():
    assert validate("192.168.1") == "False"               # Missing one block
    assert validate("192.168.1.1.1") == "False"            # Extra block
    assert validate("192.168.1.one") == "False"            # Non-numeric
    assert validate("192.168..1") == "False"               # Empty block
    assert validate("...") == "False"                      # Only dots
