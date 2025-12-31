import numpy as np
sudokuSize = 4
def print_board(board):
    for i in range(sudokuSize):
        print(board[i])

def count_empty_cells(board):
    return np.sum(board == 0)

def checkRow (board, rowNum):
    for i in range (sudokuSize):
        print("")



board = np.array([[1, 2, 3, 2],
                  [1, 4, 3, 2],
                  [1, 2, 3, 2],
                  [1, 2, 3, 2]])
empty_cells = count_empty_cells(board)

print_board(board)
print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {sudokuSize**empty_cells}")