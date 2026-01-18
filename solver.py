# Pick Empthy Square
# Try all numbers
# Find one that works
# Go to the next square and repeat
# If cannot solve backtrack (go back a sept and do not put the same number)

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
    # Finish the solve loop if the board is not comptleted
    # Find the first empty space
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range (1, len(board)+1):
        if valid(board, i, (row, column)):
            board [row][column] = i

            if solve(board):
                return True
            
            board [row][column] = 0
    return False
    

def printBoard(board):

    for i in range (len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range (len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

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
        if board[i][position[0]] == number and position[0] != i:
            return False
    
    # Check square
    # Figure out which box you are at
    boxX = position[1] // 3
    boxY = position[0] // 3
    for i in range (boxY*3, boxY*3 + 3):
        for j in range (boxX*3, boxX*3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False
    return True

printBoard(board)
print(findEmpty(board))