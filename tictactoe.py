import numpy as np
import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
ROW_COUNT = 3
COLUMN_COUNT = 3
GREEN = (0,255,0)
LEFT = 1
RIGHT = 3

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def is_valid(board, row, col):
    return board[row][col] == 0


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):

    #vertical
    r = 0
    for c in range(COLUMN_COUNT):
        if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece:
            return True
    #horizontal win condition
    c = 0
    for r in range(COLUMN_COUNT):
        if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece:
            return True
    if (board[0][0] == piece and board[1][1] == piece and board[2][2] == piece) or (board[2][0] == piece and board[1][1] == piece and board[0][2] == piece):
        return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            rect = pygame.Rect(c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if board[r][c] == 1:
                pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), Radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), Radius)
    pygame.display.update()


def check_move(x, y):
    if x < 101 and y < 101:
        row = 0
        col = 0
    elif x < 201 and y < 101:
        row = 0
        col = 1
    elif x < 301 and y < 101:
        row = 0
        col = 2
    elif x < 101 and y < 201:
        row = 1
        col = 0
    elif x < 201 and y < 201:
        row = 1
        col = 1
    elif x < 301 and y < 201:
        row = 1
        col = 2
    elif x < 101 and y < 301:
        row = 2
        col = 0
    elif x < 200 and y < 301:
        row = 2
        col = 1
    elif x < 301 and y < 301:
        row = 2
        col = 2
    rowcol = str(row) + str(col)
    return rowcol

def player_wins(p, p_color):
    text = myfont.render(p, True, p_color)
    textRect = text.get_rect()
    textRect.center = (width//2, 325)
    screen.blit(text, textRect)
    pygame.display.update()


board = create_board()
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100

Radius = int(SQUARESIZE/2 - 5)

width = COLUMN_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE + int(SQUARESIZE/2)
size = (width,height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
print(board)

myfont = pygame.font.Font("freesansbold.ttf", 32)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print(event.pos)
            if turn == 0:
                rowcol = check_move(event.pos[0], event.pos[1])
                row = int(rowcol[0])
                col = int(rowcol[1])
                if is_valid(board, row, col):
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        print("1 wins!")
                        player = "Player 1 Wins"
                        player_color = GREEN
                        player_wins(player, player_color)
                        game_over = True
                else:
                    turn = 1

            else:
                rowcol = check_move(event.pos[0], event.pos[1])
                row = int(rowcol[0])
                col = int(rowcol[1])
                if is_valid(board, row, col):
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        print("2 wins!")
                        player = "Player 2 Wins"
                        player_color = RED
                        player_wins(player, player_color)
                        game_over = True
                else:
                    turn = 0

            draw_board(board)
            print(board)
            turn += 1
            turn = turn % 2
            if game_over == True:
                pygame.time.wait(5000)
