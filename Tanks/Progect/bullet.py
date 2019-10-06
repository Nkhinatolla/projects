import threading
import pygame
from color import *
import settings

class Bullet:
	def __init__(self, x, y, tank, enemy, boxes, screen, grid):
		dx = 0
		dy = 0
		if (tank.direct == 1):
			dy = tank.reverse
		if (tank.direct == 2):
			dx = -tank.reverse
		if (tank.direct == 3):
			dy = -tank.reverse
		if (tank.direct == 4):
			dx = tank.reverse
		x += 25
		y += 25
		x += dx * 25 + dx
		y += dy * 25 + dy
		self.X = x
		self.Y = y
		self.dx = dx
		self.dy = dy
		self.clock = pygame.time.Clock()
		self.thread = threading.Thread(target=self.move, args=(tank, enemy, boxes, screen, grid))
		self.thread.start()
	def move(self, tank, enemy, boxes, screen,grid):
		while (True):
			pygame.draw.circle(screen, BLACK, (self.X, self.Y), 5)
			grid.draw(screen)
			pygame.display.update(pygame.Rect(self.X - 10, self.Y - 10, 20, 20))
			if (self.X < 0 or self.Y < 0 or self.X > 600 or self.Y > 600):
				return
			if (self.collision(enemy)):
				enemy.hp -= 1
				return
			for i in boxes:
				if (self.collision(i)):
					if (i.destroy() == True):
						pygame.draw.rect(screen, BLACK, (i.X, i.Y, settings.block, settings.block))
						boxes.remove(i)
					return
			self.X += self.dx * 5
			self.Y += self.dy * 5
			pygame.draw.circle(screen, YELLOW, (self.X, self.Y), 5)
			pygame.display.update(pygame.Rect(self.X - 10, self.Y - 10, 20, 20))
			self.clock.tick(120)

	def collision(self, object):
		if (self.X >= object.X and self.X <= object.X + 50) and (self.Y >= object.Y and self.Y <= object.Y + 50):
			return True
		return False

