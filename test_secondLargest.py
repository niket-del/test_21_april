import pytest

from secondLargest import secondlargest

def test_second_largest():
    assert secondlargest([1,4,8,4,9,5,6]) == 8
    assert secondlargest([1,4,8,4,10,9,5,6]) == 9

def test_zeros():
    assert secondlargest([0,0,0]) == float('-inf')

def test_negative():
    assert secondlargest([-1,-2,-3]) == -2

def test_all():
    assert secondlargest([-10, 1, 2, 3]) == 2

def test_single():
    assert secondlargest([5]) == float('-inf')



