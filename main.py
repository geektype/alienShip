import pygame, sys
from pygame.locals import *
from settings import *

pygame.init()
dispSurf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
gameClock = pygame.time.Clock()

def checkLaser():
    global laserX, laserY, alienX, alienY
    if (laserX > alienX-10 and laserX < alienX + 10 and laserY > alienY-10 and laserY < alienY + 10):
        alienY += 20
    return
def fireLaser():
    global laserX, laserY
    if laserY <= 0:
        laserY = shipY
        laserX = shipX


def drawLaser():
    global laserX, laserY
    if laserY >= 1:
        points = [(laserX, laserY+laserSize), (laserX, laserY)]
        pygame.draw.lines(dispSurf, WHITE, False, points, 1)
        return

def drawShip():
    x = shipX
    y = shipY
    points = [(x, y-shipSize), (x-alienSize, y+shipSize), (x+shipSize, y+shipSize)]
    pygame.draw.lines(dispSurf, GREEN, True, points, 1)
    return

def moveLaser():
    global laserY
    if laserY >= 1 :
        laserY = laserY - laserSpeed
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
    drawLaser()
    pygame.display.update()
    return

def checkKeys():
    global shipX, shipY
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        shipX = shipX - shipSpeed
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        shipX = shipX + shipSpeed
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        fireLaser()


while True:
    checkKeys()
    drawScreen()
    moveAlien()
    moveLaser()
    checkLaser()
    gameClock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()