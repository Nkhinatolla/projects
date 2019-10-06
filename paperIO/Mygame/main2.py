import pygame, os, sys
from color import *
import settings


class Hero:


	def __init__(self, X, Y, img, baseimg, direct):
		self.X = [X]
		self.Y = [Y]
		self.p = None
		self.baseX = [X]
		self.baseY = [Y]
		self.hp = 3
		self.img = img
		self.baseimg = baseimg
		self.dx = 0
		self.dy = direct


	def move(self, dx, dy):
		if (self.dx == -dx and self.dy == -dy):
			return 
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
		#print("Conuqer!")

	def defeat(self):
		if self.p:
			return True
		return False


	def update(self, enemy):
		x = self.X[-1] + self.dx
		y = self.Y[-1] + self.dy
		if (x >= 0 and x <= 600-block and y >= 0 and y <= 600-block):
			for i in range(len(self.baseX)):
				if (x == self.baseX[i] and y == self.baseY[i]):
					self.conquer()
			for i in range(len(self.X)):
				if (x == self.X[i] and y == self.Y[i]):
					self.p = True
			for i in range(len(enemy.X)):
				if (x == enemy.X[i] and y == enemy.Y[i]):
					enemy.p = True
			self.X.append(x)
			self.Y.append(y)



	def render(self, screen):
		for i in range(len(self.baseX)):
			screen.blit(self.baseimg, (self.baseX[i], self.baseY[i]))
		for i in range(len(self.X)):
			screen.blit(self.img, (self.X[i], self.Y[i]))
		



def grid():
    cells = 600 // block
    for i in range(block, 600, block):
        pygame.draw.line(screen, WHITE, (i, 0), (i, 600))
        pygame.draw.line(screen, WHITE, (0, i), (600, i))



i = Hero(0, 0, settings.pacman, settings.basepacman, 20)
j = Hero(580,580, settings.pacman1, settings.basepacman1, -20)



class GameOver:
	
	def run(self):

		if pacman.defeat() == True or manpac.defeat() == True:
			screen.fill(WHITE)
			screen.blit(settings.myy,(40,40))

			font = pygame.font.Font("freesansbold.ttf",20) 
			text = font.render("For exit tape 'Esc'", True, WHITE, BLACK)
			text2 = font.render("For continue tape 'Enter'", True, WHITE, BLACK)

			textRect = text.get_rect()
			textRect2 = text.get_rect()
			textRect.center = (100, 100)
			textRect2.center = (100,140)

			while True:
				screen.blit(text, textRect)
				screen.blit(text2, textRect2)
				pygame.display.update()

				for i in pygame.event.get():
					if i.type == pygame.KEYDOWN:
						if i.key == pygame.K_ESCAPE:
							pygame.quit()
						if i.key == pygame.K_RETURN:
							pygame.quit()
							os.system("python main2.py")
							sys.exit()
					elif i.type == pygame.QUIT:
						pygame.quit()



pygame.init()
block = 20
cells = 600 // block


screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pacman = i
manpac = j
gg = GameOver()

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
			if (i.key == pygame.K_w):
				manpac.move(0, -step)

			elif (i.key == pygame.K_DOWN):
				pacman.move(0, step)
			elif (i.key == pygame.K_s):
				manpac.move(0, step)

			elif (i.key == pygame.K_LEFT):
				pacman.move(-step, 0)
			elif (i.key == pygame.K_a):
				manpac.move(-step, 0)

			elif (i.key == pygame.K_RIGHT):
				pacman.move(step, 0)
			elif (i.key == pygame.K_d):
				manpac.move(step, 0)


	screen.blit(settings.maze, (0, 0))
	grid()
	pacman.update(manpac)
	pacman.render(screen)

	manpac.update(pacman)
	manpac.render(screen)

	gg.run()
	pygame.display.update()
	clock.tick(5)