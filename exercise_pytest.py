import pytest
import math

def test_sqr_num():
    x=10
    assert math.prod([x,x]) == 100

def test_failure():
    x=49
    assert math.sqrt(x) == 10

def test_value():
    x=100
    assert math.sqrt(x) == 11

def test_ceil():
    x=100.1
    assert math.ceil(x) == 100

