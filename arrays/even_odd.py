"""
Reorder the array so that all even numbers appear first,
followed by all odd numbers.

This is done in-place using 0(1) extra space and 0(n) time.
"""

def even_odd(A):
    next_even = 0
    next_odd = len(A)-1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1