import pygame, sys
from pygame.locals import *
from settings import *

pygame.init()
dispSurf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
gameclock = pygame.time.Clock()

def drawShip():
    x = shipX
    y = shipY
    points = [(x, y-shipSize), (x-alienSize, y+shipSize), (x+shipSize, y+shipSize)]
    pygame.draw.lines(dispSurf, GREEN, True, points, 1)
    return
def moveAlien():
    global alienDir, alienX, alienY
    if alienDir == 0:
        alienX = alienX - alienSpeed
        if alienX == 0:
            alienDir = 1
    if alienDir == 1:
        alienX = alienX + alienSpeed
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
    drawShip()
    pygame.display.update()
    return

while True:
    drawScreen()
    moveAlien()
    gameclock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()