"""
PROBLEM: Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the “pivot”) appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

Hint: Think about the partition step in quicksort
"""


def three_way_partition(A, i):
    pivot = A[i]
    low = 0
    mid = 0
    high = len(A) - 1

    while mid <= high:
        if A[mid] < pivot:
            A[low], A[mid] = A[mid], A[low]
            low += 1
            mid += 1
        elif A[mid] == pivot:
            mid += 1
        else: # A[mid] > pivot
            A[mid], A[high] = A[high], A[mid]
            high -= 1
    
    return A