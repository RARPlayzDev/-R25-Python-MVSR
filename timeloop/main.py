# TimeLoop: Puzzle Runner - Base Version
# =======================================
# Features: 
# - Player movement
# - Timer
# - Ghost clone replay system
# - One puzzle level
# - Basic UI using pygame

import pygame
import sys
import time
import json

# Configurations
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40
LOOP_DURATION = 10  # seconds
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# Level layout (0 = empty, 1 = wall, 2 = goal)
LEVEL = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.path = []

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if LEVEL[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y
            self.path.append((self.x, self.y))

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

class Ghost:
    def __init__(self, path):
        self.path = path
        self.index = 0
        self.color = GREEN
        if path:  # Ensure path isn't empty
            self.x, self.y = path[0]
        else:
            self.x, self.y = (0, 0)  # Fallback to avoid crash

    def update(self):
        if self.index < len(self.path):
            self.x, self.y = self.path[self.index]
            self.index += 1

    def draw(self):
        if self.index < len(self.path):
            pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Initialize
player = Player(1, 1, BLUE)
ghosts = []
start_time = time.time()

# Main loop
while True:
    screen.fill(BLACK)
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.move(-1, 0)
    if keys[pygame.K_RIGHT]: player.move(1, 0)
    if keys[pygame.K_UP]: player.move(0, -1)
    if keys[pygame.K_DOWN]: player.move(0, 1)

    # Update ghosts
    for ghost in ghosts:
        ghost.update()

    # Timer logic
    elapsed = time.time() - start_time
    if elapsed > LOOP_DURATION:
        ghosts.append(Ghost(player.path))
        player = Player(1, 1, BLUE)
        start_time = time.time()

    # Draw level
    for y, row in enumerate(LEVEL):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == 2:
                pygame.draw.rect(screen, RED, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw entities
    for ghost in ghosts:
        ghost.draw()
    player.draw()

    # Draw UI
    timer_text = font.render(f"Time: {max(0, int(LOOP_DURATION - elapsed))}", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
