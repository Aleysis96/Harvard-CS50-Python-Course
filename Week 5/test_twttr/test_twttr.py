from twttr import shorten

def test_error():
    assert shorten("twitter") == "twttr"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("123abc") == "123bc"



