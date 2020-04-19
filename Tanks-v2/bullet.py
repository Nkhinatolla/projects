from settings import *
import pygame




class Bullet:
    def __init__(self, x, y, direction, color):
        self.direction = direction
        self.speed = BULLET_SPEED
        self.x = x
        self.y = y
        self.radius = BULLET_RADIUS
        self.color = color
        tank_shoot = pygame.mixer.Sound('./assets/sounds/tank_shoot.wav')
        tank_shoot.set_volume(0.2)
        tank_shoot.play()

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x <= 0:
                return False
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x >= WIDTH:
                return False
        elif self.direction == Direction.UP:
            self.y -= self.speed
            if self.y <= 0:
                return False
        elif self.direction == Direction.DOWN:
            self.y += self.speed
            if self.y >= HEIGHT:
                return False
        return True

    def collision(self, x, y, width):
        if x <= self.x <= x + width:
            if y <= self.y <= y + width:
                bullet_collision = pygame.mixer.Sound('./assets/sounds/bullet_collision.wav')
                bullet_collision.play()
                return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
