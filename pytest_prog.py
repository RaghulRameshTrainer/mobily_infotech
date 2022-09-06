import pytest

def myfunc(x):
    return x+10

def test_method():
    assert myfunc(5) == 15

def test_method2():
    assert myfunc(0) == 10