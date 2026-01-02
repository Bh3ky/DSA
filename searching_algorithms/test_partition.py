from three_way_partition import three_way_partition


def is_valid_partition(arr, pivot):
    """
    Helper function:
    checks that array is partitioned as:
    < pivot | == pivot | > pivot
    """
    seen_equal = False
    seen_greater = False

    for x in arr:
        if x < pivot:
            if seen_equal or seen_greater:
                return False
        elif x == pivot:
            seen_equal = True
            if seen_greater:
                return False
        else:
            seen_greater = True

    return True


def test_basic_case():
    A = [3, 5, 2, 5, 1, 5, 4]
    i = 1  # pivot = 5
    pivot = A[i]

    result = three_way_partition(A, i)

    assert is_valid_partition(result, pivot)


def test_all_equal():
    A = [4, 4, 4, 4]
    i = 2
    pivot = A[i]

    result = three_way_partition(A, i)

    assert result == [4, 4, 4, 4]


def test_no_equals():
    A = [1, 2, 3, 4, 5]
    i = 2  # pivot = 3
    pivot = A[i]

    result = three_way_partition(A, i)

    assert is_valid_partition(result, pivot)


def test_single_element():
    A = [10]
    i = 0
    pivot = A[i]

    result = three_way_partition(A, i)

    assert result == [10]