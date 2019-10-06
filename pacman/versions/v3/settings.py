import pygame
pacman = pygame.image.load('img/packman.png')
pacman = pygame.transform.scale(pacman, (29, 29))

bots = pygame.image.load('img/bots.png')
bots = pygame.transform.scale(bots, (29, 29))

dots = pygame.image.load('img/dot.png')
dots = pygame.transform.scale(dots, (15, 15))

size = 609
cells = 21
block = size // cells

