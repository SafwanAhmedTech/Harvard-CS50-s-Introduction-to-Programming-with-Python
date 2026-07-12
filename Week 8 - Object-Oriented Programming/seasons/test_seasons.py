from seasons import minutes
import pytest

def test_minutes():
    with pytest.raises(SystemExit):
        minutes('hello')

