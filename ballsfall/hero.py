import pygame
from settings import *


class Hero:
    def __init__(self, color, pos):
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.width = pos[2]
        self.height = pos[3]
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        self.x = min(self.x, WIDTH - self.width)
        self.x = max(self.x, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))