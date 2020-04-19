import random
import pygame
from settings import *


class Ball:
    def __init__(self, r):
        self.radius = r
        self.x = random.randint(r, WIDTH - r)
        self.y = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = 5

    def move(self):
        self.y += self.speed

    def collision(self, coor):
        if coor[0] <= self.x <= coor[0] + coor[2]:
            if coor[1] <= self.y + self.radius:
                return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
