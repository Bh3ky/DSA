import pytest
from solution_1 import search

def test_target_found():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_target_not_found():
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_single_element_found():
    assert search([5], 5) == 0

def test_single_element_not_found():
    assert search([5], 3) == -1

def test_empty_array():
    assert search([], 10) == -1