import pygame
from tank import Tank
from settings import *
from colors import *


class GameState:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.tank1 = Tank(300, 300, TANK_SPEED, GREEN)
        self.tank2 = Tank(100, 100, TANK_SPEED, RED, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
        self.tanks = [self.tank1, self.tank2]
        self.bullets = []
        self.font = pygame.font.Font(None, FONT_MIN)
        self.game_over = False
        self.background = BACKGROUND

    def process(self):
        for bullet in self.bullets:

            if not bullet.move():
                self.bullets.remove(bullet)
                del bullet
                continue

            for tank in self.tanks:
                if bullet.collision(tank.x, tank.y, tank.width):
                    tank.hp -= 1
                    if tank.hp <= 0:
                        self.game_over = True
                    self.bullets.remove(bullet)
                    del bullet
                    break
        for tank in self.tanks:
            tank.move()

    def draw(self):
        self.screen.blit(BACKGROUND, (0, 0))
        for bullet in self.bullets:
            bullet.draw(self.screen)
        i = TEXT_SPACE
        for tank in self.tanks:
            text = self.font.render("HP:"+str(tank.hp), 1, tank.color)
            self.screen.blit(text, (WIDTH - text.get_size()[0] - TEXT_SPACE, i))
            tank.draw(self.screen)
            i += TEXT_SPACE + 20
