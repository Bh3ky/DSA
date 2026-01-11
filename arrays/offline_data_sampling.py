"""
PROBLEM: Implement an algorithm that takes an array of distinct elements and
a size, and returns a subset of the given size of the array elements. All subsets
should be equally likely. Return the result in input array itself.

"""

import random 

def random_subset(A, k):
    n = len(A)

    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            A[i], A[j] = A[j], A[i]
    
    return A[:k]

# approach: apply in-place algorithm (uniform random subset)
# treat the first k elements as the initial subset. for each
# remaining element at index i >= k
    # pick a random index j which is an element of [0, i]
    # and if j < k, swap A[i] with A[j]
    # the first k elements now form a uniformly random
    # subset. 








# best approach: key to building a random subset of size exactly k is to build one
# of size k-1 and then adding one more element, selected randomly from the rest. 
# Note: this is trivial when k=1
# we make one call to the random number generator, take the returned value mod n 
# (let's say it's r), and swap A[0] with A[r]. then entry A[0] now holds the result. 
# for k > 1, we begin by choosing one element at random as above and we now repeat the
# same process with the n — 1 element subarray A[1,n — 1]. eventually, the random subset
# occupies the slots A[0,k — 1] and the remaining elements are in the last n — k slots.
# intuitively, if all subsets of size k are equally likely, then the construction process
# ensures that the subsets of size k + 1 are also equally likely. A formal proof, which we
# do not present, uses mathematical induction—the induction hypothesis is that every permutation
# of every size k subset of A is equally likely to be in A[0,k — 1].

def random_sampling(k, A):
    for i in range (k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
