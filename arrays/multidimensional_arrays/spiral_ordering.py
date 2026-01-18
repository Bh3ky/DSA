"""
PROBLEM: Write a program which takes an n x n 2D array and return the spiral ordering of the array.

HINT: use case analysis and divide-and-conquer
"""

def matrix_in_spiral_order(matrix):
    n = len(matrix)
    SHIFT = [(0,1), (1,0), (0,-1), (-1,0)] # right, down, left, up

    x = y = direction = 0
    spiral = []

    for _ in range( n * n):
        spiral.append(matrix[x][y])
        matrix[x][y] = 0 # mark visited

        next_x = x + SHIFT[direction][0]
        next_y = y + SHIFT[direction][1]

        # turn if next cell is invalid or already visited
        if (next_x not in range(n) or
            next_y not in range(n) or
            matrix[next_x][next_y] == 0):
            direction = (direction + 1) % 4
            next_x = x + SHIFT[direction][0]
            next_y = y + SHIFT[direction][1]

        x, y = next_x, next_y

    return spiral 
