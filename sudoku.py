import numpy as np
sudokuSize = 4
neededTotal = 4+3+2+1
def print_board(board):
    for i in range(sudokuSize):
        print(board[i])

def count_empty_cells(board):
    return np.sum(board == 0)

# Find a better way to check them (doesnt work on 3 wrong places)
def checkRow (board, rowNum):
    total = 0
    for i in range (sudokuSize):
        total += board[rowNum][i]
    if neededTotal == total:
        print("Good row")
        return True
    else:
        print("Bad row")
        return False
    
def checkColumn (board, columnNum):
    total = 0
    for i in range (sudokuSize):
        total += board[i][columnNum]
    if neededTotal == total:
        print("Good column")
        return True
    else:
        print("Bad column")
        return False



board = np.array([[1, 2, 3, 2],
                  [1, 4, 3, 2],
                  [1, 2, 3, 2],
                  [1, 2, 3, 2]])
empty_cells = count_empty_cells(board)


checkRow(board, 0)
checkColumn(board, 1)
print_board(board)
print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {sudokuSize**empty_cells}")