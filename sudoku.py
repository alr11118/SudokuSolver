import numpy as np
sudokuSize = 3
def print_board(board):
    for i in range(sudokuSize*2):
        """""
        if i == sudokuSize:
            print("-------------")
        """""
        for j in range(sudokuSize*2):
            if j == sudokuSize:
                print("| ", end="")
            print(board[i][j], end=" ")
        print("\n")

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
