import pygame
from color import *
import settings


class Hero:


	def __init__(self, X, Y, img, baseimg):
		self.X = [X]
		self.Y = [Y]
		self.baseX = [X]
		self.baseY = [Y]
		self.hp = 3
		self.img = img
		self.baseimg = baseimg
		self.dx = 0
		self.dy = 20


	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy


	def check(self, i, j, map, was):
		if (i >= 0 and i <= cells and j >= 0 and j <= cells and map[i][j] == 0 and was[i][j] == 0):
			return True
		return False


	def conquer(self):
		map = []
		for i in range(cells + 1):
			a = [0] * (cells + 1)
			map.append(a)
		was = map.copy()
		for i in range(len(self.X)):
			self.baseX.append(self.X[i])
			self.baseY.append(self.Y[i])
		for i in range(len(self.baseX)):
			map[self.baseX[i] // block + 1][self.baseY[i] // block + 1] = 1
		
		was[0][0] = 1
		q = []
		w = []
		q.append(0)
		w.append(0)
		l = 0
		r = 0
		while (l <= r):
			i = q[l]
			j = w[l]
			if (self.check(i - 1, j, was, map) == True):
				q.append(i - 1)
				w.append(j)
				r += 1
				was[i - 1][j] = 1
			if (self.check(i, j - 1, was, map) == True):
				q.append(i)
				w.append(j - 1)
				r += 1
				was[i][j - 1] = 1
			if (self.check(i + 1, j, was, map) == True):
				q.append(i + 1)
				w.append(j)
				r += 1
				was[i + 1][j] = 1
			if (self.check(i, j + 1, was, map) == True):
				q.append(i)
				w.append(j + 1)
				r += 1
				was[i][j + 1] = 1
			l += 1
		for i in range(cells + 1):
			for j in range(cells + 1):
				if (was[i][j] == 0 and map[i][j] == 0):
					self.baseX.append((i - 1) * block)
					self.baseY.append((j - 1) * block)
		self.X.clear()
		self.Y.clear()
		print("Conuqer!")


	def defeat(self):
		print("Died")


	def update(self):
		x = self.X[-1] + self.dx
		y = self.Y[-1] + self.dy
		if (x >= 0 and x <= 600-block and y >= 0 and y <= 600-block):
			for i in range(len(self.baseX)):
				if (x == self.baseX[i] and y == self.baseY[i]):
					self.conquer()
			for i in range(len(self.X)):
				if (x == self.X[i] and y == self.Y[i]):
					self.defeat()	
			self.X.append(x)
			self.Y.append(y)


	def render(self, screen):
		for i in range(len(self.X)):
			screen.blit(self.img, (self.X[i], self.Y[i]))
		for i in range(len(self.baseX)):
			screen.blit(self.baseimg, (self.baseX[i], self.baseY[i]))



def grid():
    cells = 600 // block
    for i in range(block, 600, block):
        pygame.draw.line(screen, WHITE, (i, 0), (i, 600))
        pygame.draw.line(screen, WHITE, (0, i), (600, i))
pygame.init()
block = 20
cells = 600 // block
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pacman = Hero(0, 0, settings.pacman, settings.basepacman)

lastKey = None
step = 20


while (True):

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
		elif i.type == pygame.KEYDOWN:
			if (i.key == pygame.K_ESCAPE):
				pygame.quit()
			if (i.key == pygame.K_UP):
				pacman.move(0, -step)
			elif (i.key == pygame.K_DOWN):
				pacman.move(0, step)
			elif (i.key == pygame.K_LEFT):
				pacman.move(-step, 0)
			elif (i.key == pygame.K_RIGHT):
				pacman.move(step, 0)
	# screen.blit(setting.smaze, (0, 0))
	grid()
	pacman.update()
	pacman.render(screen)
	pygame.display.update()
	clock.tick(5)