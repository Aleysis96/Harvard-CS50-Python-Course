from um import count

def test_valid_count():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("um, thanks") == 1
    assert count("Um, thanks for the album.") == 1

def test_invalid_count():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("This is my new album") == 0

def test_multiple_um():
    assert count("Um... um, well, um.") == 3
    assert count("um, my name is..um, alex and..um, i from...um, mexico") == 4

