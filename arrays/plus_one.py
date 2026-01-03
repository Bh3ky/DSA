# INCREMENT AN ARBITRARY-PRECISION INTEGER

"""
PROBLEM: Write a program which takes as input an array of digits encoding a decimal integer D and updates
the array to represent the integer D + 1. For example, if the input is (1,2,9) then you should update
the array to (1,3,0). Your algorithm should work even if it is implemented in a language that has
finite-precision arithmetic.

Hint: Experiment with concrete examples.
"""

from typing import List

def plus_one(digits: List[int]) -> List[int]:
    """
    Increment an arbitray-precision integer represented
    as a list of digits.

    Args:
        digits (List[int]): List of digits representing
        a decimal integer.

    Return:
        List[int]: Unpaid list of digits representing
        the integer + 1. 
    """

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits 