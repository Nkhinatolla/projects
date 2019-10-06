import pygame
pacman = pygame.image.load('img/pacman.png')
pacman = pygame.transform.scale(pacman, (20, 20))


basepacman = pygame.image.load('img/basepacman.png')
basepacman = pygame.transform.scale(basepacman, (20, 20))


pacman1 = pygame.image.load("img/pacman1.png")
pacman1 = pygame.transform.scale(pacman1, (20,20))


basepacman1 = pygame.image.load("img/basepacman1.png")
basepacman1 = pygame.transform.scale(basepacman1, (20,20))


maze = pygame.image.load('img/maze.png')
maze = pygame.transform.scale(maze, (600, 600))

myy = pygame.image.load('img/gameover.png')
myy = pygame.transform.scale(myy,(500,500))