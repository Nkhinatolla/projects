from enum import Enum
from colors import *
import pygame


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


WIDTH = 600
HEIGHT = 600


TANK_WIDTH = 40
TANK_SPEED = 2
TANK_HP = 3

BULLET_SPEED = 6
BULLET_RADIUS = 5


FONT_MIN = 36
FONT_MAX = 60
TEXT_SPACE = 20


BACKGROUND = pygame.image.load('./assets/images/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
