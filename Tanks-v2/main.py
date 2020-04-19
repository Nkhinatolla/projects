import pygame
from game_state import GameState
from settings import *
from colors import *

pygame.init()
game = GameState()
loop = True

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.game_over = True
            if event.key == pygame.K_RETURN:
                game.bullets.append(game.tank1.shoot())
            if event.key == pygame.K_SPACE:
                game.bullets.append(game.tank2.shoot())
            for tank in game.tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])

    game.process()
    game.draw()
    pygame.display.update()

font = pygame.font.Font(None, FONT_MAX)
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
    text = font.render("GAME OVER", 1, LIGHT_BLUE)
    game.screen.blit(text, (WIDTH // 2 - text.get_size()[0] // 2, HEIGHT // 2 - text.get_size()[1] // 2))
    pygame.display.update()
pygame.quit()
