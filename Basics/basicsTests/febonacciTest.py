#import pytest

from Basics.febbonacci import febonacci

def test_feb():
    assert febonacci(5) == [0, 1, 1, 2, 3]

def test_feb_negative_Value():
    assert febonacci(-5) == [0, 1]
