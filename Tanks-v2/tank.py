import pygame
from settings import *
from bullet import Bullet


class Tank:

    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = TANK_WIDTH
        self.direction = Direction.RIGHT
        self.hp = TANK_HP
        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self, screen):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x + self.width <= 0:
                self.x = WIDTH
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x >= WIDTH:
                self.x = -self.width
        elif self.direction == Direction.UP:
            self.y -= self.speed
            if self.y + self.width <= 0:
                self.y = HEIGHT
        elif self.direction == Direction.DOWN:
            self.y += self.speed
            if self.y >= HEIGHT:
                self.y = -self.width

    def shoot(self):
        if self.direction == Direction.RIGHT:
            return Bullet(self.x + self.width // 2 + self.width, self.y + self.width // 2, self.direction, self.color)
        if self.direction == Direction.LEFT:
            return Bullet(self.x + self.width // 2 - self.width, self.y + self.width // 2, self.direction, self.color)
        if self.direction == Direction.UP:
            return Bullet(self.x + self.width // 2, self.y + self.width // 2 - self.width, self.direction, self.color)
        if self.direction == Direction.DOWN:
            return Bullet(self.x + self.width // 2, self.y + self.width // 2 + self.width, self.direction, self.color)
