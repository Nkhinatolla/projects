import pygame
from game_state import GameState

pygame.init()
game = GameState()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
    keys = pygame.key.get_pressed()
    game.process()
    game.hero.move(keys)
    game.draw()
    pygame.display.update()

