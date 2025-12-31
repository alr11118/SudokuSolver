import numpy as np
sudokuSize = 4
neededTotal = 4+3+2+1
def print_board(board):
    for i in range(sudokuSize):
        print(board[i])

def count_empty_cells(board):
    return np.sum(board == 0)

# Checks if there is any repeated numbers in ROWS
def checkRow (board, rowNum):
    row = board[rowNum]
    for i in range (len(row)):
        for j in range (i+1, len(row)):
            if row[j] == row[i]:
                #print("Bad row")
                return False
    #print("Good row")
    return True 
# Checks if there is any repeated numbers in COLUMNS
def checkColumn (board, ColumnNum):
    column = board[ColumnNum]
    for i in range (len(column)):
        for j in range (i+1, len(column)):
            if column[j] == column[i]:
                #print("Bad column")
                return False
    #print("Good column")
    return True 

def checkBoard (board):
    for i in range(sudokuSize):
        if (checkRow(board, i) != True):
            print("Board is bad")
            return False
        if (checkColumn(board, i) != True):
            print("Board is bad")
            return False
    print("Board is good")
    return True

board = np.array([[1, 4, 3, 2],
                  [3, 2, 1, 4],
                  [4, 1, 2, 3],
                  [2, 3, 4, 1]])
board2 = np.array([[1, 4, 3, 2],
                   [3, 4, 1, 4],
                   [4, 1, 2, 3],
                   [2, 3, 4, 1]])
empty_cells = count_empty_cells(board)

checkBoard(board)
checkBoard(board2)
print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {sudokuSize**empty_cells}")