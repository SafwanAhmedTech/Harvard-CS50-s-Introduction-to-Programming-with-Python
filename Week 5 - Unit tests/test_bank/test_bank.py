from bank import value
def test_hello():
    assert value('hello') == 0
def test_h():
    assert value('hi') == 20
def test_normal():
    assert value('good day') == 100
def test_punct():
    assert value('hello!') == 0
def test_numbers():
    assert value('1') == 100
def test_cases():
    assert value('HELLO') == 0
