""""
PROBLEM: Check whether a 9 x 9 2D array representing a partially completed Sudoku is valid.
Specifically, check that no row, column, or 3 x 3 2D subarray contains duplicates.
A 0-value in the 2D array indicates that entry is blank; every other entry is in [1,9].

Hint: Directly test the constraints. Use an array to encode sets.
"""

def is_valid_sudoku(board):
    rows = [[False] * 10 for _ in range(9)]
    cols = [[False] * 10 for _ in range(9)]
    boxes = [[False] * 10 for _ in range(9)]

    # Check each cell only once (traversing).
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == 0: # 0 indicates blank cell
                continue

            # index mapping   
            box_index = (r // 3) * 3 + (c // 3)

            # if the value has already appeared in:
                # in the row, column, and the 3x3 box
            # then the Sudoku board is invalid
            if rows[r][value] or cols[c][value] or boxes[box_index][value]:
                return False
            
            # mark the value as appeared in the row, column, and the 3x3 box
            rows[r][value] = True
            cols[c][value] = True
            boxes[box_index][value] = True
    
    # if no duplicates found, the Sudoku board is valid
    return True



