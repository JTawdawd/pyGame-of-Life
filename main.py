import pygame
import numpy as np
import patterns

CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
PRIMARY_COLOR = (255, 255, 255)
SECONDARY_COLOR = (0, 0, 0)
FRAME_GAP = 100

grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
grid = patterns.Pulsar(grid)

def update_grid():
    new_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            num_neighbors = (
                grid[(i-1)%GRID_WIDTH][(j-1)%GRID_HEIGHT] +
                grid[(i-1)%GRID_WIDTH][j] +
                grid[(i-1)%GRID_WIDTH][(j+1)%GRID_HEIGHT] +
                grid[i][(j-1)%GRID_HEIGHT] +
                grid[i][(j+1)%GRID_HEIGHT] +
                grid[(i+1)%GRID_WIDTH][(j-1)%GRID_HEIGHT] +
                grid[(i+1)%GRID_WIDTH][j] +
                grid[(i+1)%GRID_WIDTH][(j+1)%GRID_HEIGHT]
            )

            if grid[i][j] == 1 and (num_neighbors == 2 or num_neighbors == 3):
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and num_neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

def draw_grid():
     for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            if grid[i][j] == 1:
                color = PRIMARY_COLOR
            else:
                color = SECONDARY_COLOR
            pygame.draw.rect(screen, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

pygame.init()

screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Game of Life")
font = pygame.font.Font(None, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    grid = update_grid()
    draw_grid()
    
    pygame.display.update()
    pygame.time.wait(FRAME_GAP)
    
pygame.quit()
