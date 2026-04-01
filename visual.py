import sys
import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)

screenWidth, screenHeight = 1000, 750
screen = pygame.display.set_mode((screenWidth, screenHeight))

headerFont = pygame.font.SysFont('Arial', 20, pygame.font.Font.bold)
headerText = headerFont.render("Sudoku Solver", 1, BLACK)

gameFont = pygame.font.SysFont('Arial', 20)

def drawScreen(gameBoard):
    screen.fill(WHITE)

    screen.blit(headerText, (screenWidth//2 - headerText.get_width()//2, 10))

    startX = 150
    startY = 150

    for row in range(9):
        for col in range(9):
            rect = pygame.Rect(50*col + startX, 50*row + startY, 50, 50)
            pygame.draw.rect(screen, GREY, rect, 1)

            val = gameBoard[row][col]
            if val != 0:
                text = gameFont.render(str(val), True, BLACK)
                screen.blit(text, text.get_rect(center=rect.center))

    pygame.display.update()


def update(gameBoard):
    # Handle quit so window doesn't freeze
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    drawScreen(gameBoard)
    pygame.time.delay(30)  # control speed