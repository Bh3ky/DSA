"""
PROBLEM: Write a program which takes as input a non-negative integer n and returns 
the first n rows of Pascal's triangle.
"""

class Solution:
    def generate_pascal_triangle(self, n):
        # intiialize the 2D array with 1s
        result = [[1] * (i + 1) for i in range(n)] 

        # fill in the inner elements of the triangle
        for i in range(2, n):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        return result


# Brute-force solution would be to organise the arrays in memory similar to how they appear
# in the figure (Pascal's triangle).
# time complexity: O(n^2)
# space complexity: O(n^2)