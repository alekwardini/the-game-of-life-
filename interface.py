import pygame 
import time
from sys import exit

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

while True:
    for i in pygame.event.get():
        if i == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
