import pytest

from List.maxMin import findMaxMin

def test_normal_case():
    assert findMaxMin([5, 7, 12, 15, 12, 19]) == {'maximum': 19, 'minimum': 5}


def test_single_element():
    assert findMaxMin([10]) == {'maximum': 10, 'minimum': 10}


def test_negative_numbers():
    assert findMaxMin([-5, -10, -3, -8]) == {'maximum': -3, 'minimum': -10}

def test_mixed_numbers():
    assert findMaxMin([-1, 0, 5, -10, 8]) == {'maximum': 8, 'minimum': -10}

def test_all_same():
    assert findMaxMin([4, 4, 4, 4]) == {'maximum': 4, 'minimum': 4}

