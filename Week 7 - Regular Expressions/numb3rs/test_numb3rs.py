from numb3rs import validate
def test_correct():
    assert validate('2.2.2.2') == True
def test_incorrect():
    assert validate('275.3.3.3') == False
    assert validate('s.s.s.s') == False
