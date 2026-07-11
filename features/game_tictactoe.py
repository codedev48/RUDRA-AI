# file name: complex_maze_game.py
import pygame
import sys

# ------------------ CONFIG ------------------ #
BLOCK_SIZE = 20
ROWS, COLS = 15, 30
WIDTH, HEIGHT = COLS*BLOCK_SIZE, ROWS*BLOCK_SIZE
FPS = 10

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Complex Maze layout (1=wall, 0=path)
# 15 rows x 30 columns
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

START = (1,1)
GOAL = (28,13)
# ------------------------------------------- #

def draw_maze(win, player_pos):
    win.fill(BLACK)
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if cell == 1:
                pygame.draw.rect(win, BLUE, rect)
            elif (x,y) == GOAL:
                pygame.draw.rect(win, GREEN, rect)
    # Player
    player_rect = pygame.Rect(player_pos[0]*BLOCK_SIZE, player_pos[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(win, RED, player_rect)
    pygame.display.update()

def play_complex_maze():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RUDRA Complex Maze Game")
    clock = pygame.time.Clock()

    player_pos = list(START)
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        next_pos = player_pos.copy()
        if keys[pygame.K_LEFT]:
            next_pos[0] -= 1
        elif keys[pygame.K_RIGHT]:
            next_pos[0] += 1
        elif keys[pygame.K_UP]:
            next_pos[1] -= 1
        elif keys[pygame.K_DOWN]:
            next_pos[1] += 1
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # Collision
        if 0 <= next_pos[1] < ROWS and 0 <= next_pos[0] < COLS:
            if MAZE[next_pos[1]][next_pos[0]] == 0 or (next_pos[0], next_pos[1]) == GOAL:
                player_pos = next_pos

        draw_maze(win, player_pos)

        # Check win
        if tuple(player_pos) == GOAL:
            font = pygame.font.SysFont("Arial", 40)
            win.fill(BLACK)
            text = font.render("YOU WIN!", True, GREEN)
            win.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 20))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False

    pygame.quit()

# ---------- RUN GAME ---------- #
if __name__ == "__main__":
    play_complex_maze()