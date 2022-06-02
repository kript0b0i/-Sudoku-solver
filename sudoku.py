 from pprint import pprint

def find_next_empty(puzzle):
    """
    It returns the row and column of the next empty cell in the puzzle
    
    :param puzzle: the puzzle to solve
    :return: The row and column of the next empty cell.
    """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    """
    If the guess is not in the row, column, or 3x3 box, then it's valid.
    
    :param puzzle: the puzzle we're trying to solve
    :param guess: the number we're trying to place in the puzzle
    :param row: the row of the cell we're trying to fill
    :param col: the column we're currently working on
    :return: A boolean value
    """
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False


    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    """
    If there are no empty cells, return True. Otherwise, try all possible guesses for the next empty
    cell, and if any of them work, return True
    
    :param puzzle: The puzzle to solve
    :return: a boolean value.
    """
    row, col = find_next_empty(puzzle)
    
    pprint(example_board)
    print("------------")

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
        
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
        [-1, 8, -1,   7, -1, 1,   -1, 3, -1],
        [4, -1, 9,   -1, -1, -1,   -1, -1, -1],
        [-1, 5, -1,   -1, 6, -1,   4, 1, 8],

        [7, -1, -1,   -1, -1, 9,   -1, -1, -1],
        [8, -1, -1,   6, 1, -1,   5, -1, -1],
        [-1, 3, 5,   -1, -1, -1,   -1, 2, 9],

        [-1, 6, -1,   4, -1, 7,   -1, 9, -1],
        [1, -1, -1,   -1, -1, 8,   -1, -1, 4],
        [-1, 2, -1,   -1, 5, -1,   -1, 7, -1]
    ]
    solve_sudoku(example_board)
    pprint(example_board)
