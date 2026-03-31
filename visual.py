import sys

import pygame
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)

screenWidth, screenHeight = 1000, 750
screen = pygame.display.set_mode((screenWidth, screenHeight))

headerFont = pygame.font.SysFont('Arial', 20, pygame.font.Font.bold)
headerText = headerFont.render("Welcome to my Sudoku Solver!", 1, BLACK)

gameFont = pygame.font.SysFont('Arial', 15, pygame.font.Font.bold)

squares = [[None for _ in range(9)] for _ in range(9)] #creates a 9x9 structure

gameBoard1 = [[9, 6, 0, 7, 0, 8, 0, 0, 5],
             [0, 0, 5, 0, 4, 0, 6, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 9, 0],
             [0, 9, 0, 0, 0, 2, 5, 0, 0],
             [0, 0, 0, 9, 1, 0, 0, 0, 4],
             [2, 0, 0, 0, 0, 0, 0, 3, 6],
             [5, 0, 0, 0, 0, 0, 0, 0, 3],
             [0, 0, 9, 0, 0, 0, 0, 8, 0],
             [8, 2, 0, 0, 0, 0, 0, 0, 9]]
 
sellectedSquare = None


FPS = 60

def printGameBoard(gameBoard):
    startX = 150
    startY = 150
    for row in range(0, 9):
        for column in range(0, 9):
            squares[row][column] = pygame.Rect(50*column + startX, 50*row + startY, 50, 50)
            pygame.draw.rect(screen, GREY, squares[row][column], 2)
            numText = gameFont.render(str(gameBoard[row][column]), True, BLACK)
            numRect = numText.get_rect(center= squares[row][column].center)
            screen.blit(numText, numRect)
            """"
            numText = gameFont.render(("[" + str(row)+ ", " + str(column) + "]"), True, BLACK)
            numRect = numText.get_rect(center= squares[row][column].center)
            screen.blit(numText, numRect)
            """
    for row in range(1, 4):
        for column in range(1, 4):
            pygame.draw.rect(screen, BLACK, (150*column, 150*row, 150, 150), 3)
    pygame.draw.rect(screen, BLACK, (150, 150, 450, 450), 6)
    

def drawScreen(gameBoard):
    screen.fill(WHITE)
    screen.blit(headerText, (screenWidth//2 - headerText.get_width()//2, 10))
    printGameBoard(gameBoard)
    if sellectedSquare != None:
        pygame.draw.rect(screen, GREEN, sellectedSquare, 2)
    pygame.display.update()

def main(gameBoard):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawScreen(gameBoard)

if __name__ == "__main__":
    main()
