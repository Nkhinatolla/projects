import pygame

size = 609
cells = 21
block = size // cells

pacman = pygame.image.load('img/pacman.png')
pacman = pygame.transform.scale(pacman, (block, block))

bots = pygame.image.load('img/bots.png')
bots = pygame.transform.scale(bots, (block, block))
