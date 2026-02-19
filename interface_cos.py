import pygame 
import time
from sys import exit
from main import gen 

pygame.init()
width, height = int(input("Rentrez la largeur de la fenêtre : ")), int(input("Rentrez la hauteur de la fenêtre : "))
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

coordinates = [] 
simulation_active = False

green_button = pygame.Rect(10, 10, 40, 40)
red_button = pygame.Rect(60, 10, 40, 40)
blue_button = pygame.Rect(110, 10, 40, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if green_button.collidepoint(mouse_pos):
                simulation_active = True
            elif red_button.collidepoint(mouse_pos):
                simulation_active = False
            elif blue_button.collidepoint(mouse_pos):
                coordinates = []
                simulation_active = False
            else:
                grid_x = (mouse_pos[0] // 10) * 10
                grid_y = (mouse_pos[1] // 10) * 10
                
                if (grid_x, grid_y) in coordinates:
                    coordinates.remove((grid_x, grid_y))
                else:
                    coordinates.append((grid_x, grid_y))

    if simulation_active:
        coordinates = gen(coordinates)
        time.sleep(0.3)

    screen.fill(BLACK)

    for x in range(0, width, 10):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height))
    for y in range(0, height, 10):
        pygame.draw.line(screen, GRAY, (0, y), (width, y))

    for x, y in coordinates:
        pygame.draw.rect(screen, GREEN, (x, y, 10, 10))

    pygame.draw.rect(screen, GREEN, green_button)
    pygame.draw.rect(screen, RED, red_button)
    pygame.draw.rect(screen, BLUE, blue_button)
    
    pygame.display.update()