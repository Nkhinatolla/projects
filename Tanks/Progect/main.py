import pygame
from pygame.locals import *
import settings
from color import *
import grid
from tank import Tank #class
from bullet import Bullet
import threading

from box import createBoxes #function

def tablo():
    pygame.draw.rect(screen, BLACK, (675, 50, 75, 200))
    screen.blit(settings.t1Icon, (650, 50))
    for i in range(25, tank1.hp * 25 + 1, 25):
        screen.blit(settings.heartImg, (650 + i, 50))
    
    textsurface = myfont.render(str(round(tank1.reload, 2)), False, WHITE)
    screen.blit(textsurface,(650,100))
    
    screen.blit(settings.t2Icon, (650, 150)) 
    for i in range(25, tank2.hp * 25 + 1, 25):
        screen.blit(settings.heartImg, (650 + i, 150))

    textsurface = myfont.render(str(round(tank2.reload, 2)), False, WHITE)
    screen.blit(textsurface,(650,200))

    pygame.display.update(pygame.Rect(675, 50, 75, 200))

pygame.init()
clock = pygame.time.Clock()

pygame.font.init()  
myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
tank1 = Tank(0, 0, settings.t1Img, 3, -1)
tank2 = Tank(settings.width - settings.block, settings.height - settings.block, settings.t2Img, 3, 1)
boxes = createBoxes()




screen = pygame.display.set_mode((settings.width + 200, settings.height))

play = True
while (play):
    circB = pygame.draw.rect(screen, BLACK, (tank1.X, tank1.Y, settings.block, settings.block))
    circB = pygame.draw.rect(screen, BLACK, (tank2.X, tank2.Y, settings.block, settings.block))
    grid.draw(screen)
    for i in pygame.event.get():
        if i.type == QUIT or (i.type == KEYDOWN and i.key == K_ESCAPE):
            play = False
        elif i.type == KEYDOWN:
            if i.key == K_DOWN:
                tank2.move(1,screen, grid, boxes, tank1)
            elif i.key == K_UP:
                tank2.move(3,screen, grid, boxes, tank1)
            elif i.key == K_LEFT:
                tank2.move(2,screen,grid, boxes, tank1)
            elif i.key == K_RIGHT:
                tank2.move(4,screen,grid, boxes, tank1)
            elif i.key == K_s:
                tank1.move(3,screen,grid, boxes, tank2)
            elif i.key == K_a:
                tank1.move(4,screen,grid, boxes, tank2)
            elif i.key == K_w:
                tank1.move(1,screen, grid, boxes, tank2)
            elif i.key == K_d:
                tank1.move(2,screen,grid, boxes, tank2)
            elif i.key == K_SPACE:
                if (tank1.reload == 0):
                    Bullet(tank1.X, tank1.Y, tank1, tank2, boxes, screen, grid)
                    threading.Thread(target=tank1.Reload, args=()).start()
            elif i.key == K_p:
                if (tank2.reload == 0): 
                    Bullet(tank2.X, tank2.Y, tank2, tank1, boxes, screen, grid)
                    threading.Thread(target=tank2.Reload, args=()).start()

    screen.blit(tank1.img, (tank1.X, tank1.Y)) 
    screen.blit(tank2.img, (tank2.X, tank2.Y)) 
    for i in boxes:
        screen.blit(i.img, (i.X, i.Y)) 
    
    pygame.display.update()
    tablo()
    clock.tick(settings.FPS)