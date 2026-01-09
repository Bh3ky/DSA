"""
PROBLEM: Compute the kth permutation under dictionary ordering, starting from the
identity permutation (which is the first permutation in dictionary ordering).
"""

class Solution:
    def getPermutation(self, n, k):
        """
        Returns the k-th permutation (1-based) of the identity permutation [0, 1, ..., n-1]
        """

        # Convert k to 0-based index
        k -= 1

        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Numbers to use
        numbers = list(range(n))
        result = []

        for i in range(n, 0, -1):
            block_size = factorial[i - 1]
            index = k // block_size

            result.append(numbers[index])
            numbers.pop(index)

            k %= block_size

        return result