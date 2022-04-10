import copy
from numpy import unsignedinteger
import pygame
import time

pygame.init()

class gamestate:
    window = 800
    sq = unsignedinteger
    sqsize = unsignedinteger
    thisgen = []
    newgen = []

class color:
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255,255,255)

def fillboard():
    for y in range(gamestate.sq):
            gamestate.thisgen.append([])
            for x in range(gamestate.sq):
                gamestate.thisgen[y].append(0)

def drawboard(screen):

    for y in range(gamestate.sq):
        for x in range(gamestate.sq):
            pygame.draw.rect(screen, color.black, pygame.Rect(
                x * gamestate.sqsize, y * gamestate.sqsize, gamestate.sqsize - 1, gamestate.sqsize - 2))
            if gamestate.thisgen[y][x] == 1:
                pygame.draw.rect(screen, color.white, pygame.Rect(
                x * gamestate.sqsize, y * gamestate.sqsize, gamestate.sqsize - 1, gamestate.sqsize - 2))

    pygame.draw.line(screen, color.white, (0,0),(0,gamestate.window),1)
    pygame.draw.line(screen, color.white, (0,0),(gamestate.window,0),1)

def selectcell(y, x,):
    if gamestate.thisgen[y][x] == 0:
        gamestate.thisgen[y][x] = 1
    else:
        gamestate.thisgen[y][x] = 0

def switchcell(y, x,):
    if gamestate.newgen[y][x] == 0:
        gamestate.newgen[y][x] = 1
    else:
        gamestate.newgen[y][x] = 0

def nextgen():
    gamestate.newgen = copy.deepcopy(gamestate.thisgen)
    for y in range(gamestate.sq):
        for x in range(gamestate.sq):
            sum = count(y, x)
            if sum >= 4 and gamestate.thisgen[y][x] == 1:
                switchcell(y, x)
            if sum == 3 and gamestate.thisgen[y][x] == 0:
                switchcell(y, x,)
            if sum <= 1 and gamestate.thisgen[y][x] == 1:
                switchcell(y, x,)
    gamestate.thisgen = gamestate.newgen


def count(y, x):
    sum = 0
    try:
        if gamestate.thisgen[y-1][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y-1][x] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y-1][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y+1][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y+1][x] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if gamestate.thisgen[y+1][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    return sum


def gameoflife():
    print("Grid Size: ")
    gamestate.sq = int(input())
    gamestate.sqsize = gamestate.window / gamestate.sq
    screen = pygame.display.set_mode((gamestate.window, gamestate.window))
    clock = pygame.time.Clock()
    screen.fill(color.white)
    fillboard()
    drawboard(screen)
    clock.tick(15)
    pygame.display.flip()
    running = True
    play = False
    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                y = int(click[1] // gamestate.sqsize)
                x = int(click[0] // gamestate.sqsize)
                selectcell(y,x)
                
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    nextgen()
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    if play == True:
                        play = False
                    else:
                        play = True
        
        if play == True:
            nextgen()
            time.sleep(0.1)

        drawboard(screen)
        pygame.display.flip()

gameoflife()