import pygame
import time

# --- INITIALIZATION ---
pygame.init()
CELL_SIZE = 30
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

coordinates = [(10,10), (11,10), (12,10), (12,9), (11,8)] # A "Glider" shape
next_generation = []

def surround(i, j):
    counter = 0
    # We check the current 'coordinates' list for neighbors
    # This checks the 8 spots around (i, j)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0: continue # Skip the cell itself
            if (i + dx, j + dy) in coordinates:
                counter += 1
    
    # Rules logic
    if (i, j) in coordinates: # If currently alive
        return counter in (2, 3)
    else: # If currently dead
        return counter == 3

# --- MAIN LOOP ---
running = True
while running:
    # 1. Handle Events (Allow closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Logic Step (Your code logic)
    for i in coordinates:
        # Check the cell itself and all 8 neighbors for potential life
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                target = (i[0] + dx, i[1] + dy)
                if target not in next_generation:
                    if surround(target[0], target[1]):
                        next_generation.append(target)
    
    coordinates = next_generation.copy()
    next_generation = []

    # 3. Drawing Step
    screen.fill((20, 20, 20)) # Dark gray background
    
    for cell in coordinates:
        # Map logic (x,y) to pixels
        rect = (cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
        pygame.draw.rect(screen, (0, 255, 100), rect) # Neon green cells

    pygame.display.flip()
    
    # Slow it down so we can see the evolution
    time.sleep(0.7) 

pygame.quit()