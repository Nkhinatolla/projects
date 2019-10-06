import pygame

WIDTH = 609
HEIGHT = 609
FPS = 10
block = WIDTH // 21

level = 1


#images
tank = pygame.image.load("img/tank.png")
tank = pygame.transform.scale(tank, (block, block))
tankUP = pygame.transform.rotate(tank, 90)
tankDOWN = pygame.transform.rotate(tank, -90)
tankRIGHT = pygame.transform.rotate(tank, 0)
tankLEFT = pygame.transform.rotate(tank, 180)

enemy = pygame.image.load("img/tank.png")
enemy = pygame.transform.scale(enemy, (block, block))
enemyUP = pygame.transform.rotate(enemy, 90)
enemyDOWN = pygame.transform.rotate(enemy, -90)
enemyRIGHT = pygame.transform.rotate(enemy, 0)
enemyLEFT = pygame.transform.rotate(enemy, 180)


common = pygame.image.load("img/common1.png")
common = pygame.transform.scale(common, (block, block))

common2 = pygame.image.load("img/common2.png")
common2 = pygame.transform.scale(common2, (block, block))

common3 = pygame.image.load("img/common3.png")
common3 = pygame.transform.scale(common3, (block, block))

immortal = pygame.image.load("img/immortal.png")
immortal = pygame.transform.scale(immortal, (block, block))

ghost = pygame.image.load("img/ghost.png")
ghost = pygame.transform.scale(ghost, (block, block))