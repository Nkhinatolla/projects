import pygame
import settings
from pygame.locals import *




class Hero:
	def __init__(self, type, x = 0, y = 0):
		self.X = x
		self.Y = y
		self.destX = x
		self.destY = y
		self.bomb_r = 150
		self.bomb_n = 5
		self.bombs = 0
		self.type = type
		self.score = 0
		self.alive = True
		if type == 1:
			self.img = settings.heroImg
		else:
			self.img = settings.enemyImg
	
	def smoothMove(self, grid, surface, clock, bombs):
		dx = 0
		dy = 0
		if self.X > self.destX:
			dx = -1
		elif self.X < self.destX:
			dx = 1
		if self.Y > self.destY:
			dy = -1
		elif self.Y < self.destY:
			dy = 1
		while (self.X != self.destX or self.Y != self.destY):
			rect = pygame.Rect(self.X, self.Y, settings.ICON, settings.ICON)
			surface.fill((0,0,0))
			grid.draw(surface)
			for i in bombs:
				surface.blit(i.img, (i.X, i.Y))
			surface.blit(settings.heroImg, (self.X, self.Y))
			pygame.display.update(rect)
			self.X += dx
			self.Y += dy
			clock.tick(150)
		
