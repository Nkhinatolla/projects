import pygame
from color import *
import settings
import threading
import random, sys

def inFrame(x, y):
	if (x >= 0 and x <= size - block and y >= 0 and y <= size - block):
		return True
	return False

class Hero:
	def __init__(self, X, Y, img):
		self.X = X
		self.Y = Y
		self.hp = 3
		self.img = img
		self.dx = 0
		self.dy = 0
	def move(self, dx, dy):
		x = self.X + dx
		y = self.Y + dy
		coorX = x // block
		coorY = y // block
		if (coorX == -1 and coorY == 9):
			coorX = 20
		if (coorX == 21 and coorY == 9):
			coorX = 0
		x = coorX * block
		y = coorY * block
		if (inFrame(x, y) and level.map[coorY][coorX] == '.'):
			self.X = x
			self.Y = y
			if ((coorX, coorY) in level.points):
				level.points.remove((coorX, coorY))
	def render(self):
		screen.blit(self.img, (self.X, self.Y))

class Enemy:
	def __init__(self, X, Y, img):
		self.X = X
		self.Y = Y
		self.img = img
		self.dx = 0
		self.dy = 0
		self.destX = X
		self.destY = Y
		self.ways = [] 
		self.clock = pygame.time.Clock()
		self.thread = threading.Thread(target=self.move, args=[])
		self.thread.start()
	def go(self, x, y, x1, y1, was, query, put):
		if (x < 0 or x >= cells or y < 0 or y >= cells):
			return
		if (level.map[y][x] == '#' or was[x][y] != -1):
			return
		was[x][y] = was[x1][y1] + 1
		put[x][y] = [x1, y1].copy()
		query.append([x, y])
	def updateDest(self , rdX = -1, rdY = -1):
		if (rdX == -1):
			rdX = random.randint(0, cells - 1)
			rdY = random.randint(0, cells - 1)
		was = []
		put = []
		while (True):
			for i in range(cells):
				a = [-1] * cells
				b = []
				for j in range(cells):
					b.append([-1])
				was.append(a)
				put.append(b)
			was[self.X // block][self.Y // block] = 0
			put[self.X // block][self.Y // block] = [0, 0]
			query = [[self.X // block, self.Y // block]]
			i = 0
			[[0, 1, 2, 3],
			 [1, 2, 3, 4]
			]
			[[[0, 0], [0, 0], [0, 1], [0 2]],
			[]]

			while (i < len(query)):
				x = query[i][0]
				y = query[i][1]
				self.go(x - 1, y, x, y, was, query, put)
				self.go(x + 1, y, x, y, was, query, put)
				self.go(x, y + 1, x, y, was, query, put)
				self.go(x, y - 1, x, y, was, query, put)
				i += 1
			if (was[rdX][rdY] == -1):
				rdX = random.randint(0, cells - 1)
				rdY = random.randint(0, cells - 1)
				was = []
				put = []
			else:
				break			
		self.ways = []
		self.destX = rdX * block
		self.destY = rdY * block
		while(put[rdX][rdY] != [0, 0]):
			if (put[rdX][rdY] == [-1]):
				break
			self.ways.append([rdX, rdY])
			rdX = put[rdX][rdY][0]
			rdY = put[rdX][rdY][1]
	def move(self):
		while (True):
			if (self.destX == self.X and self.destY == self.Y):
				self.updateDest()
			if (self.X == pacman.X or self.Y == pacman.Y):
				self.updateDest(pacman.X // block, pacman.Y // block)
			self.X = self.ways[-1][0] * block
			self.Y = self.ways[-1][1] * block
			self.ways.pop()
			self.clock.tick(3)
	def render(self):
		screen.blit(self.img, (self.X, self.Y))

class Level:
	def __init__(self, currentLVL = 1):
	 	self.currentLVL = currentLVL
	 	self.points = []
	def loadMap(self):
		f = open("levels/level" + str(self.currentLVL), "r")
		self.map = f.read().split("\n")
		for i in range(len(map)):
			for j in range(len(map[i])):
				if (map[i][j] == '.'):
					self.points.append((i, j))
	def render(self):
		screen.fill(BLACK)
		map = self.map
		for i in range(len(map)):
			for j in range(len(map[i])):
				if (map[i][j] == '.'):
					pygame.draw.rect(screen, BLACK, (j * block, i * block, block, block))
				else:
					pygame.draw.rect(screen, LIGHT_BLUE, (j * block, i * block, block, block))
		for i, j in self.points:
			
#class Dots:
	def __init__(self, img):
		self.randomDest()
	 	self.img = img
	 def randomDest(self):
	 	rX =
	 	rY = 
	 	while(level.map[Y][X] != '.'):
	 		rX =
	 		rY = 
	 	self.X = rX * block
	 	self.Y = rY * block
	#def setoffood(self):
		#crf = []
		#for i in range (cells):
			#for j in range(cells):
				#if (level.map[i][j] == '.'): 
					#crf.append([x,y])
	#def eat(self.X)
	#def render(self):
		#for i in range(len(level.map)):
			#for j in range(len(level.map[i])):
				#if (level.map[i][j] == '.'):
					#screen.blit(self.img, (self.X, self.Y))


pygame.init()
size = settings.size
screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
cells = settings.cells
block = settings.block
level = Level()
level.loadMap()
pacman = Hero(10 * block , 15 * block, settings.pacman)
#dots = Dots(10 * block , 10 * block, settings.dots)
bots = []
number_of_bots = 1		
for i in range(number_of_bots):
	bots.append(Enemy(2 * block, 1 * block, settings.bots)) 

lastKey = []


while (True):
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
		elif i.type == pygame.KEYDOWN:
			if (i.key == pygame.K_ESCAPE):
				pygame.quit()
			lastKey.append(i.key)
		elif i.type == pygame.KEYUP:
			lastKey.remove(i.key)
	if (len(lastKey) > 0):
		if (lastKey[-1] == pygame.K_UP):
			pacman.move(0, -block)
		elif (lastKey[-1] == pygame.K_DOWN):
			pacman.move(0, block)
		elif (lastKey[-1] == pygame.K_LEFT):
			pacman.move(-block, 0)
		elif (lastKey[-1] == pygame.K_RIGHT):
			pacman.move(block, 0)
	level.render()
	for i in bots:
		i.render()
	pacman.render()
	#dots.render()
	pygame.display.update()
	clock.tick(8)
	

