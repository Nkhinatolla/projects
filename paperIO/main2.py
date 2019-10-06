import pygame, os, sys
from color import *
import settings
from pygame.locals import *


class Hero:


	def __init__(self, X, Y, img, baseimg, direct, baseX, baseY):
		self.X = [X]
		self.Y = [Y]
		self.alive = False
		self.baseX = baseX
		self.baseY = baseY
		self.hp = 3
		self.img = img
		self.baseimg = baseimg
		self.dx = 0
		self.dy = direct


	def move(self, dx, dy):

		if self.dx == -dx and self.dy == -dy:
			return 

		if 600 < self.X[-1] < 0 or  600 < self.Y[-1] < 0:
			self.alive = True

		self.dx = dx
		self.dy = dy


	def check(self, i, j, map, was):


		if (i >= 0 and i <= cells + 1 and j >= 0 and j <= cells + 1 and map[i][j] == 0 and was[i][j] == 0):
			return True
		return False


	def conquer(self, enemy,x,y):
		map = []
		for i in range(cells + 2):
			a = [0] * (cells + 2)
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



		for i in range(cells + 2):
			for j in range(cells + 2):
				if (was[i][j] == 0 and map[i][j] == 0):
					self.baseX.append((i - 1) * block)
					self.baseY.append((j - 1) * block)
					for h in range(len(enemy.baseX)):
						if (i - 1) * block == enemy.baseX[h] and (j - 1) * block == enemy.baseY[h]:
							enemy.baseX.pop(h)
							enemy.baseY.pop(h)
							break



		self.X.clear()
		self.Y.clear()
		#print("Conuqer!")

	def defeat(self):
		if self.alive:
			return True
		return False


	def update(self, enemy):

		x = self.X[-1] + self.dx
		y = self.Y[-1] + self.dy


		if (x >= 0 and x <= 600-block and y >= 0 and y <= 600-block):

			for i in range(len(self.baseX)):
				if (x == self.baseX[i] and y == self.baseY[i]):
					self.conquer(enemy, self.baseX[i] ,self.baseY[i])

			for i in range(len(self.X)):
				if (x == self.X[i] and y == self.Y[i]):
					self.alive = True
			for i in range(len(enemy.X)):
				if (x == enemy.X[i] and y == enemy.Y[i]):
					enemy.alive = True
			for i in range(len(enemy.baseX)):
				if (enemy.baseX[i] == x and enemy.baseY[i] == y):
					enemy.baseX.pop(i)
					enemy.baseY.pop(i)
					break
			
			self.X.append(x)
			self.Y.append(y)

		else:
			self.alive = True


	def render(self, screen):
		for i in range(len(self.X)):
			screen.blit(self.img, (self.X[i], self.Y[i]))

	def renderbase(self, screen):
		for i in range(len(self.baseX)):
			screen.blit(self.baseimg, (self.baseX[i], self.baseY[i]))
		



def grid():
    cells = 600 // block
    for i in range(block, 600, block):
        pygame.draw.line(screen, WHITE, (i, 0), (i, 600))
        pygame.draw.line(screen, WHITE, (0, i), (600, i))


def createHero():
	global pacman, manpac
	if (pacman == None or pacman.alive == True):
		pacman = Hero(0, 0, settings.pacman, settings.basepacman, 20, [0, 1 * block, 0, 1 * block], [0, 0, 1 * block, 1 * block])
	if (manpac == None or manpac.alive == True):
		manpac = Hero(580,580, settings.pacman1, settings.basepacman1, -20, [600 - block, 600 - 2 * block, 600 - block, 600 - 2 * block], [600 - block, 600 - block, 600 - 2 * block, 600 - 2 * block])


def run():
	if pacman.defeat() == True or manpac.defeat() == True:
		createHero()
			

pygame.init()
block = 20
cells = 600 // block


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pacman = None
manpac = None

createHero()

lastKey = None
step = 20

while (True):
	pressed = pygame.key.get_pressed()
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
		elif i.type == pygame.KEYDOWN:
			if (i.key == pygame.K_ESCAPE):
				pygame.quit()

			if (i.key == pygame.K_UP):
				manpac.move(0, -step)
			if (i.key == pygame.K_w):
				pacman.move(0, -step)

			elif (i.key == pygame.K_DOWN):
				manpac.move(0, step)
			elif (i.key == pygame.K_s):
				pacman.move(0, step)

			elif (i.key == pygame.K_LEFT):
				manpac.move(-step, 0)
			elif (i.key == pygame.K_a):
				pacman.move(-step, 0)

			elif (i.key == pygame.K_RIGHT):
				manpac.move(step, 0)
			elif (i.key == pygame.K_d):
				pacman.move(step, 0)


		font = pygame.font.Font("freesansbold.ttf",20) 
		text = font.render("{} : {}".format(len(pacman.baseX),len(manpac.baseX)), True, WHITE, BLACK)

		textRect = text.get_rect()
		textRect.center = (700,50)

		screen.blit(pacman.baseimg, (675, 60))
		screen.blit(manpac.baseimg, (710, 60))
		screen.blit(text, textRect)



	screen.blit(settings.maze, (0, 0))
	
	grid()
	manpac.update(pacman)
	manpac.renderbase(screen)
	pacman.update(manpac)
	pacman.renderbase(screen)


	pacman.render(screen)
	manpac.render(screen)

	run()
	pygame.display.update()
	clock.tick(15)