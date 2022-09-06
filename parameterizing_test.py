import pytest

@pytest.mark.parametrize("x,output",[(5,10),(10,20),(100,500),(200,400)])
def test_calc(x,output):
    assert 2*x == output