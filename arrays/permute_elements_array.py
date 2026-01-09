# permutation is a rearrangement of members of a sequence into a new sequence.
# can be applied to an array to reorder the array. 

"""
PROBLEM: Given an array A of n elements and a permuatation P, apply P to A.

Hint: any permutation can be viewed as a set of cyclic permutations. For an 
element in a cycle, how would you identify if it has been permuted?
"""

def apply_permutation(perm, A):
    for i in range(len(A)):
        # we check to see if the element at index i
        # has not been moved by checking if perm[i]
        # is non-negative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # now we subtract len(perm) from an entry in
            # perm to make it negative, which indicates
            # the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    
    # restore perm
    perm[:] = [a + len(perm) for a in perm]

# Note: the program above will apply the permutation in O(n) time.
# The space complexity is O(1), assuming we can temporarily modify
# the sign bit from entries in the permutation array.
