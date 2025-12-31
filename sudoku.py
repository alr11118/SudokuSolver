import numpy as np
import random
sudokuSize = 4
# Prints the board in a demure and readable way 
def print_board(board):
    for i in range(sudokuSize):
        print(board[i])

# Counts the number of empty shells
def count_empty_cells(board):
    return np.sum(board == 0)


# Checks if there is any repeated numbers in ROWS
def checkRow (board, rowNum):
    row = board[rowNum]
    for i in range (len(row)):
        for j in range (i+1, len(row)):
            if row[j] == row[i] or row[i] > sudokuSize or row[i] < 1:
                #print("Bad row")
                return False
    #print("Good row")
    return True 

# Checks if there is any repeated numbers in COLUMNS
def checkColumn (board, ColumnNum):
    column = board[:, ColumnNum]
    for i in range (len(column)):
        for j in range (i+1, len(column)):
            if column[j] == column[i] or column[i] > sudokuSize or column[i] < 1:
                #print("Bad column")
                return False
    #print("Good column")
    return True 

# Checks board for unavlible placements using the checkColumn() and checkRow()
def checkBoard (board):
    for i in range(sudokuSize):
        if (checkRow(board, i) != True):
            #print("Board is bad")
            return False
        if (checkColumn(board, i) != True):
            #print("Board is bad")
            return False
    #print("Board is good")
    return True

Eboard = np.array([[1, 4, 3, 2],
                   [3, 0, 1, 4],
                   [4, 1, 2, 3],
                   [2, 3, 4, 1]])

empty_cells = count_empty_cells(Eboard)
emptyCoordinates = np.argwhere(Eboard == 0)

checkBoard(Eboard)

print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {sudokuSize**empty_cells}")
print (emptyCoordinates)


# Try Many Random Solutions
solved = False
numAttempts = 0
while (solved != True and numAttempts < 100000):
    # Generate/reset the solution set
    test = Eboard.copy()
    numAttempts +=1
    # Generate the posible conbination & Place it 
    for j in range (empty_cells):
        #posible = np.append(posible, random.randint(1, sudokuSize))
        test [emptyCoordinates[j]] = random.randint(1, sudokuSize)
        #print(posible)

    # Test it & Return the current one if it works
    if (checkBoard(test) == True):
        print_board(test)
        solved = True

print("Not solved")