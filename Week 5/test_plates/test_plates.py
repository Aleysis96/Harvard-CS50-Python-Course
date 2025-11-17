from plates import is_valid

def test_plates():
    assert is_valid("taco") == True
    assert is_valid("CS50") == True

def test_too_short():
    assert is_valid("A") == False

def test_too_long():
    assert is_valid("ABCDEFG") == False

def test_invalid():
    assert is_valid("1ABC") == False

def test_non_alphanumeric():
    assert is_valid("AB@123") == False

def without_beginning_alphabetical():
    assert is_valid("!AB123") == False
    assert is_valid("1A2B3C") == False

def test_leading_zero_in_number():
    assert is_valid("AB012") == False

def test_invalid_number_placement():
    assert is_valid("AB12C") == False
