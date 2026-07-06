from plates import is_valid
def test_length():
    assert is_valid('a') == False
def test_numbers():
    assert is_valid('AAA22A') == False
def test_punct():
    assert is_valid('ABC!FJ') == False
def test_letters():
    assert is_valid('22ABDI') == False
    assert is_valid('AABCD5') == True
def test_zero():
    assert is_valid('ABCD02') == False
