import pytest

def test_nums():
    x=100
    y=200
    assert x<y

@pytest.mark.xfail
def addnum():
    x=10
    y=20
    assert x+y > 100

@pytest.mark.skip
def test_val():
    x=100
    assert x<1000