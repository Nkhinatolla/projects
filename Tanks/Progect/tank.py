import settings
from color import *
import threading
import pygame
import time
class Tank:
	def __init__(self, coorX, coorY, img, direct, r):
		self.X = coorX
		self.Y = coorY
		self.img = img
		self.simg = img
		self.reload = 0
		self.hp = 3
		self.direct = direct
		self.reverse = r
		self.drive = False
	def move(self, direct, screen, grid, boxes, enemy):
		if (direct == 1):
			self.img = pygame.transform.rotate(self.simg, 180)
		if (direct == 2):
			self.img = pygame.transform.rotate(self.simg, 90)
		if (direct == 3):
			self.img = self.simg
		if (direct == 4):
			self.img = pygame.transform.rotate(self.simg, -90)
		if (direct != self.direct):
			self.direct = direct
			return
		if (self.drive == False):
			self.thread = threading.Thread(target=self.smoothmove, args = (screen,grid, boxes, enemy))
			self.thread.start()
	def smoothmove(self, screen, grid, boxes, enemy):
		dx = 0
		dy = 0
		if (self.direct == 1):
			dy = self.reverse
		if (self.direct == 2):
			dx = -self.reverse
		if (self.direct == 3):
			dy = -self.reverse
		if (self.direct == 4):
			dx = self.reverse
		x = self.X + dx * 50
		y = self.Y + dy * 50
		if (x < 0 or y < 0 or x > 550 or y > 550):
			return
		if ((enemy.X, enemy.Y) == (x, y)):
			return
		for i in boxes:
			if (i.X, i.Y) == (x, y):
				return
		self.drive = True
		i = 1
		while (i <= 50):
			circB = pygame.draw.rect(screen, BLACK, (self.X, self.Y, settings.block, settings.block))
			grid.draw(screen)
			pygame.display.update(pygame.Rect(self.X, self.Y, settings.block, settings.block))
			self.X += dx
			self.Y += dy
			screen.blit(self.img, (self.X, self.Y))
			i += 1
			pygame.display.update(pygame.Rect(self.X, self.Y, settings.block, settings.block))
		self.drive = False
		return
	def Reload(self):
		stime = time.time()
		# self.reload = 1
		# while (time.time() - stime < 1):
		# 	self.reload = 1 - (time.time() - stime)
		self.reload = 0
