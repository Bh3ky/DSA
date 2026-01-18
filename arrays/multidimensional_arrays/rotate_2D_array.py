"""
PROBLEM: Write a function that takes as input an n xn 2D array, and rotates the array by 90 degrees clockwise.

Hint: Focus on the boundary elements. 
"""

def rotate_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n -1 - layer

        for i in range(first, last):
            offset = i - 1

            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top 
