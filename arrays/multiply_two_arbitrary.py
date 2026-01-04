"""
PROBLEM: Write a program that takes two arrays representing integers,
and returns an integer represent- ing their product. 
"""

def multiply(A, B):
    # handle zero shortcut (early exit)
    # WHY?? prevent weird edge cases since
    # we already know that any number x 0
    # is zero. 
    if A == [0] or B == [0]:
        return [0]
    
    # determine the sign
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1 # ^ = XOR (true only if one side is TRUE)

    # work with absolute values
    A[0], B[0] = abs(A[0]), abs(B[0]) # allow us to work with only positive digits
    n, m = len(A), len(B) # stores the lengths of the inputs

    # result array -> n + m represent the most possible product
    result = [0] * (n + m)

    # multiply digits
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            result[i + j + 1] += A[i] * B[j]
            # handles the carry
            result[i + j] += result[i + j + 1] // 10 
            result[i + j + 1] %= 10

    # remove loading zeros
    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    # applying the sign
    if sign == -1:
        result[0] = -result[0]

    return result
