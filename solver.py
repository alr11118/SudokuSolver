import visual
import time

# Pick Empthy Square
# Try all numbers
# Find one that works
# Go to the next square and repeat
# If cannot solve backtrack (go back a sept and do not put the same number)
sudoku_size = 3
board = [
    [7, 0, 0, 0, 0, 1, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 4, 0, 5, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0]
]

board4 = [
        [3, 0, 4, 0],
        [0, 1, 0, 2],
        [0, 4, 0, 3],
        [2, 0, 1, 0]
]

def solve(board):
    # Finish the solve loop if the board is not comptleted
    # Find the first empty space
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, column = find

    # Try all values for that empty space
    for i in range (1, len(board)+1):
        # If that value is valid add that to the board
        if valid(board, i, (row, column)): 
            board[row][column] = i
            printBoard(board)
            #time.sleep(0.05)
            #printBoard(board)
            #print("")

            # Call on solve again recursevly untill the board is solved
            if solve(board):
                return True
            
            # If the call to solve doest work backtarck by setting the last variable to 0
            board [row][column] = 0
    # If the current call to solve cannot find a valid value return false to backtrack in the previus loop
    return False
    
def printBoard(board):
    visual.main(board)

    """
    for i in range (len(board)):
        if i % sudoku_size == 0 and i != 0:
            print("------------------------")
        for j in range (len(board[0])):
            if j % sudoku_size == 0 and j != 0:
                print(" | ", end="")

            if j == (sudoku_size*sudoku_size -1):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    """

def findEmpty(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == 0:
                return (i, j) # (row, column) 
    return None

def valid(board, number, position):
    # Check row
    for i in range (len(board[0])):  # Loop tru the columns of that row
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check Column
    for i in range (len(board)):  # Loop tru the rows of that column
        if board[i][position[1]] == number and position[0] != i:
            return False
    
    # Check square
    # Figure out which box you are at
    boxX = position[1] // sudoku_size
    boxY = position[0] // sudoku_size
    for i in range (boxY*sudoku_size, boxY*sudoku_size + sudoku_size):
        for j in range (boxX*sudoku_size, boxX*sudoku_size + sudoku_size):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

printBoard(board)
solve(board)
print(" ")
printBoard(board)
