import pygame
from hero import Hero
from balls import Ball
from settings import *
from colors import *
import time


class GameState:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hero = Hero(YELLOW, START_POSITION)
        self.balls = []
        self.last_time = 0
        self.score = 0
        self.font = pygame.font.Font(None, BASE_FONT_SIZE)

    def process(self):
        if time.time() - self.last_time >= 1:
            self.balls.append(Ball(BASE_RADIUS))
            self.last_time = time.time()
        for ball in self.balls:
            if ball.collision((self.hero.x, self.hero.y, self.hero.width, self.hero.height)):
                self.score += 1
                self.balls.remove(ball)
                del ball
                continue
            if ball.collision((0, HEIGHT + ball.radius * 2, WIDTH, 0)):
                self.balls.remove(ball)
                del ball
                continue

            ball.move()

    def draw(self):
        self.screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(self.screen)

        text = self.font.render("score: " + str(self.score), 1, RED)
        self.screen.blit(text, (WIDTH - text.get_size()[0] - 20,  20))
        self.hero.draw(self.screen)
