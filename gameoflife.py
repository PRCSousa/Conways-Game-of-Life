import pygame
import numpy

pygame.init()

class board:
    sq = 50
    board = []

class color:
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255,255,255)

def fillboard():
    for y in range(board.sq):
            board.board.append([])
            for x in range(board.sq):
                board.board[y].append(0)

def drawboard(screen):

    for y in range(board.sq):
        for x in range(board.sq):
            pygame.draw.rect(screen, color.black, pygame.Rect(
                x * board.sq, y * board.sq, board.sq - 1, board.sq - 2))
            if board.board[y][x] == 1:
                pygame.draw.rect(screen, color.white, pygame.Rect(
                x * board.sq, y * board.sq, board.sq - 1, board.sq - 2))

    pygame.draw.line(screen, color.white, (0,0),(0,800),1)
    pygame.draw.line(screen, color.white, (0,0),(800,0),1)

def switchcell(y, x):
    if board.board[y][x] == 0:
        board.board[y][x] = 1
    else:
        board.board[y][x] = 0

def nextgen():
    #Code Here
    for y in range(board.sq):
        for x in range(board.sq):
            sum = count(y, x)
            if sum >= 4:
                board.board[y][x] = 0
            if sum == 3 or sum == 2:
                board.board[y][x] = 1
            if sum <= 1:
                board.board[y][x] = 0
            if sum == 0:
                board.board[y][x] = 0


def count(y, x):
    sum = 0
    try:
        if board.board[y-1][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y-1][x] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y-1][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y+1][x-1] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y+1][x] == 1:
            sum += 1
    except IndexError:
        pass
    try:
        if board.board[y+1][x+1] == 1:
            sum += 1
    except IndexError:
        pass
    return sum





def gameoflife():
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    screen.fill(color.white)
    fillboard()
    # print(board.board)
    drawboard(screen)
    clock.tick(15)
    pygame.display.flip()
    running = True
    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                running = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                y = int(click[1] // board.sq)
                x = int(click[0] // board.sq)
                # print(yi, xi)
                switchcell(y,x)
                
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    nextgen()

        drawboard(screen)
        pygame.display.flip()

gameoflife()