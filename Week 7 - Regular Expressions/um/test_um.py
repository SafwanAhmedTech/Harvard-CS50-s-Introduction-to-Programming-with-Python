from um import count
def test_correct():
    assert count('um i am um') == 2

def test_caps():
    assert count('UM i am Um') == 2

def test_none():
    assert count('1') == 0
    assert count('i am!') == 0
    assert count('yummy') == 0
