import pygame, sys
from pygame.locals import *
from settings import *

pygame.init()
dispSurf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

def moveAlien():
    global alienDir, alienX, alienY
    if alienDir == 0:
        alienX = alienX - 1
        if alienX == 0:
            alienDir = 1
    if alienDir == 1:
        alienX = alienX + 1
        if alienX == WIDTH:
            alienDir = 0


def drawAlien():
    x = alienX
    y = alienY
    points = [(x, y+alienSize), (x-alienSize, y-alienSize), (x+alienSize, y-alienSize)]
    pygame.draw.lines(dispSurf, RED, True, points, 1)
    return

def drawScreen():
    dispSurf.fill(BLACK)
    drawAlien()
    pygame.display.update()
    return

while True:
    drawScreen()
    moveAlien()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()