from seasons import get_minutes

def test_valid_minutes():
    assert get_minutes("1996-06-27") == "Fifteen million, four hundred thirty-six thousand, eight hundred minutes"
    assert get_minutes("1999-01-01") == "Fourteen million, one hundred fourteen thousand, eight hundred eighty minutes"
    assert get_minutes("2020-06-01") == "Two million, eight hundred fifty-one thousand, two hundred minutes"

