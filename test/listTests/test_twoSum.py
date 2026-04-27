import pytest

from List.twoSum import twoSum


def test_two_sum():
    assert twoSum([2,7,11, 15, 3],9) == [0, 1]
def test_two_sum_negative():
    assert twoSum([2,-7,11, 15, -3],9) == -1
def test_two_sum_zero():
    assert twoSum([0,0,0,0,0],0) == [0,1]
def test_empty_list():
    assert twoSum([],0) == -1
def test_no_output():
    assert twoSum([2,7,11,5],0) == -1
def test_Single_input():
    assert twoSum([5],5) == -1
def test_num_twice():
    assert twoSum([5,5],10) == [0,1]
def test_multiple_valid():
    assert twoSum([1,2,3,4],5) == [1,2]

