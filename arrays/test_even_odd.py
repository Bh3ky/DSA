import random
from even_odd import even_odd

def is_valid_partition(arr):
    """
    Verifies all even appears before odds.
    Orders within group does NOT matter.
    """
    seen_odd = False
    for x in arr:
        if x % 2 == 1:
            seen_odd = True
        if seen_odd and x % 2 == 0:
            return False
    return True



# ---------------- BASIC TESTS ----------------

def test_mixed_values():
    arr = [3, 2, 4, 1, 5, 6]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_already_partitioned():
    arr = [2, 4, 6, 1, 3, 5]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_all_even():
    arr = [2, 4, 6, 8]
    even_odd(arr)
    assert arr == [2, 4, 6, 8]


def test_all_odd():
    arr = [1, 3, 5, 7]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_empty_array():
    arr = []
    even_odd(arr)
    assert arr == []


def test_single_element_even():
    arr = [2]
    even_odd(arr)
    assert arr == [2]


def test_single_element_odd():
    arr = [1]
    even_odd(arr)
    assert arr == [1]


# ---------------- EDGE CASES ----------------

def test_duplicates():
    arr = [2, 2, 1, 1, 2, 1]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_negative_numbers():
    arr = [-3, -2, -1, -4, 5, 6]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_zero_handling():
    arr = [0, 1, 2, 3, 0, 5]
    even_odd(arr)
    assert is_valid_partition(arr)


# ---------------- STRESS TESTS ----------------

def test_large_random_array():
    arr = [random.randint(-10**6, 10**6) for _ in range(100_000)]
    even_odd(arr)
    assert is_valid_partition(arr)


def test_worst_case_alternating():
    arr = [1, 2] * 50_000
    even_odd(arr)
    assert is_valid_partition(arr)


def test_reverse_worst_case():
    arr = list(range(1, 100_001))  # odds and evens mixed
    even_odd(arr)
    assert is_valid_partition(arr)