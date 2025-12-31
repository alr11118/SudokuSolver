import numpy as np
sudokuSize = 3
def print_board(board):
    for i in range(sudokuSize*2):
        print(board[i])

def count_empty_cells(board):
    return np.sum(board == 0)

"""""Example usage:
board = [[5, 3, 0, 0, 7, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 0],
         [8, 0, 0, 0, 6, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 0],
         [0, 0, 0, 4, 1, 9, 0, 5]]
"""
board = np.array([[1, 2, 0, 0, 3, 2],
                  [1, 2, 0, 0, 3, 2],
                  [1, 2, 0, 0, 3, 2],
                  [1, 2, 0, 0, 3, 2],
                  [1, 2, 0, 0, 3, 2],
                  [1, 2, 0, 0, 3, 2]])
print_board(board)
empty_cells = count_empty_cells(board)
print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {3**empty_cells}")