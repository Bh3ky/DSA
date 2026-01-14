"""
PROBLEM: Design an algorithm that creates uniformly random permutations of {0,1,...,n —1}. You are given
a random number generator that returns integers in the set {0,1,.. .,W — 1} with equal probability;
use as few calls to it as possible.

Hint: If the result is stored in A, how would you proceed once A[n — 1] is assigned correctly?
"""

import random

def compute_random_permutation(n):
    # start with 0 to n-1 in order
    A = list(range(n))

    # build the permutation one position at a time
    for i in range(n):
        # pick a random index from the remaining part
        j = random.randint(i, n - 1)

        # swap
        A[i], A[j] = A[j], A[i]

    return A