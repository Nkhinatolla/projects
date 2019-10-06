import pygame
import settings

def draw(screen):
    for i in range(settings.block, settings.width + 1, settings.block):
        pygame.draw.line(screen, (255, 255, 255), [0, i], [settings.height, i])
    for i in range(settings.block, settings.width + 1, settings.block):
        pygame.draw.line(screen, (255, 255, 255), [i, 0], [i, settings.height])