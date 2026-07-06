from twttr import shorten
def test_upper_and_lower():
    assert shorten('HEllo i am ronaldo') == 'Hll  m rnld'
    assert shorten('HELLO i AM ronALdo and i am') == 'HLL  M rnLd nd  m'

def test_numbers():
    assert shorten('a123b') == '123b'

def test_punct():
    assert shorten('HEllo i am ronaldo!!!') == 'Hll  m rnld!!!'
