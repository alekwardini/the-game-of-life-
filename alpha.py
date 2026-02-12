import time
import pygame 
import sys

coordinates = [(0,0), (1,0), (0,1), (1,1), (4,5)]
next_generation = []
def surround(i, j):
    counter = 0
    alive  = True
    if (i+1, j) in coordinates: counter += 1 

    if (i-1, j) in coordinates:  counter += 1 
    if (i+1, j+1) in coordinates:  counter += 1 
    if (i-1, j+1) in coordinates:  counter += 1 
    if (i+1, j-1) in coordinates:  counter += 1 
    if (i- 1, j-1) in coordinates:  counter += 1 
    if (i, j+1) in coordinates:  counter += 1 
    if (i, j-1) in coordinates:  counter += 1 
    if counter not in (2, 3):
        alive = False
    if counter == 3:
        alive = True
    return alive
while True:
    for i in coordinates:
        if surround(i[0], i[1]) == True and (i[0], i[1]) not in next_generation:
            next_generation.append(i)
        if surround(i[0]+1, i[1]) == True and (i[0]+1, i[1]) not in next_generation:
            next_generation.append((i[0]+1 , i[1]))
        if surround(i[0]+1, i[1]) == True and (i[0]+1, i[1]) not in next_generation:
            next_generation.append((i[0]+1 , i[1]))
        if surround(i[0]+1, i[1]-1) == True and (i[0]+1, i[1]-1) not in next_generation:
            next_generation.append((i[0]+1 , i[1]-1))
        if surround(i[0]+1, i[1]+1) == True and (i[0]+1, i[1]+1) not in next_generation:
            next_generation.append((i[0]+1 , i[1]+1))
        if surround(i[0]+1, i[1]) == True and (i[0]+1, i[1]) not in next_generation:
            next_generation.append((i[0]-1 , i[1]))
        if surround(i[0]-1, i[1]+1) == True and (i[0]-1, i[1]+1) not in next_generation:
            next_generation.append((i[0]-1 , i[1]+1))
        if surround(i[0]-1, i[1]-1) == True and (i[0]-1, i[1]-1) not in next_generation:
            next_generation.append((i[0]-1 , i[1]-1))
        if surround(i[0], i[1]+1) == True and (i[0], i[1]+1) not in next_generation:
            next_generation.append((i[0] , i[1]+1))
        if surround(i[0], i[1]-1) == True and (i[0], i[1]-1) not in next_generation:
            next_generation.append((i[0] , i[1]-1))
    coordinates = next_generation.copy()
    next_generation = []
    print(coordinates)
    time.sleep(5)
print(next_generation)