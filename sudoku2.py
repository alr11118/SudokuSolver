# ONLY WORKS FOR 4X4 BOARDS
import numpy as np
sudokuSize = 4
neededList = np.array([1, 2, 3, 4])

board = np.array([[1, 4, 3, 2],
                  [3, 0, 1, 4],
                  [4, 1, 2, 3],
                  [2, 3, 4, 1]])

# Creates the Squares for later checking
def checkSquares(board, sudokuSize):
    square1 = np.array([board[0][0], board[0][1], board[1][0], board[1][1]])
    print(square1)
    square2 = np.array([board[0][2], board[0][3], board[1][2], board[1][3]])
    print(square2)
    square3 = np.array([board[2][0], board[2][1], board[3][0], board[3][1]])
    print(square3)
    square4 = np.array([board[2][2], board[2][3], board[3][2], board[3][3]])
    print(square4)
    for i in range (sudokuSize):
        #Add aparantesis to make it organised
        if neededList[i] in square1 and neededList[i] in square2 and neededList[i] in square3 and neededList[i] in square4:
            pass
        else:
            return False
    return True

# Prints the board in a demure and readable way 
def print_board(board):
    for i in range(sudokuSize):
        print(board[i])

#Test these functions!!!!!!!!!
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



# Is it really necesarry????
# Counts the number of empty shells
def count_empty_cells(board):
    return np.sum(board == 0)

# Checks board for unavlible placements using the checkColumn() and checkRow()
def checkBoard (board):
    if (checkSquares(board, sudokuSize) != True):
            print("Board is bad because of squares")
            return False
    for i in range(sudokuSize):
        if (checkRow(board, i) != True):
            print("Board is bad")
            return False
        if (checkColumn(board, i) != True):
            #rint("Board is bad")
            return False
    print("Board is good")
    return True



empty_cells = count_empty_cells(board)
emptyCoordinates = np.argwhere(board == 0)

checkBoard(board)

print(f"Number of empty cells: {empty_cells}")
print(f"number of possible combinations {sudokuSize**empty_cells}")
print (emptyCoordinates)

#Find where cordinates are 0
# Go trough rows and coulnms if they have any 0's in them is so how many
# if there is just one zero (creat a fix function earlier) and fix it    
# OR make a fix function that is called on 0 points that tryes fixing buy row and does if there is more then 2 msiing in the row tryies fixing by coumn and if that doesnt work leaves it as it is.
# The fix method gets called on 0 points as long as they exist and finds 0 points everyloop.
#(edit the check functions to return an int (0-infinty) to show how many pieces are missin on that row??? 
# OR ) 


