import pygame 
import sys

CELL_SIZE = 10 

def surround(i, j, current_coords):
    counter = 0
    neighbor_offsets = [
        (10, 0), (-10, 0), (10, 10), (-10, 10),
        (10, -10), (-10, -10), (0, 10), (0, -10)
    ]
    
    for dx, dy in neighbor_offsets:
        if (i + dx, j + dy) in current_coords:
            counter += 1
    
    if (i, j) in current_coords:
        return counter in (2, 3)
    else:
        return counter == 3

def gen(current_coords):
    next_gen = []
    potential_cells = set()
    for i, j in current_coords:
        potential_cells.add((i, j))
        for dx in [-10, 0, 10]:
            for dy in [-10, 0, 10]:
                potential_cells.add((i + dx, j + dy))
    
    for cell in potential_cells:
        if surround(cell[0], cell[1], current_coords):
            if cell not in next_gen:
                next_gen.append(cell)
    
    return next_gen