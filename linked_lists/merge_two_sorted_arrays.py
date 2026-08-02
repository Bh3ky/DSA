"""
Question: Write a Python function called merge_sorted() that takes already sorted
lists of integers and returns a single sorted list containing all the elements 
from both lists
"""

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    merged: list[int] = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if  a[i] <= b[j]:
            # append a[i] then move the pointer
            merged.append(a[i])
            i += 1
        else:
            # append b[j] the move the pointer
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged

# Time complexity: O(n + m) since we only touched each element exactly once
# Space complexity: O(n + m) since we created a new list called merged containing all elements

# Test cases

# Typical case

assert merge_sorted([1, 4, 7], [2, 3, 5]) == [1, 2, 3, 4, 5, 7]

# Both lists empty

assert merge_sorted([], []) == []

# First list empty

assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]

# Second list empty

assert merge_sorted([1, 2, 3], []) == [1, 2, 3]

# Duplicate values

assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

# Negative numbers

assert merge_sorted([-5, -2], [-3, 1]) == [-5, -3, -2, 1]

# Lists with different lengths

assert merge_sorted([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# First list entirely smaller

assert merge_sorted([1, 2, 3], [10, 11]) == [1, 2, 3, 10, 11]

print("All tests passed")