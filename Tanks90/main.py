import pygame
from pygame.locals import *
from colors import *
from settings import *

class Tank:
	def __init__(self, X, Y, img, direct):
		self.X = X
		self.Y = Y
		self.img = img
		self.direct = direct
	def move(self, dx, dy, enemy):	
		direct = self.direct
		if (dx == 0 and dy == block):
			self.direct = 2
		if (dx == 0 and dy == -block):
			self.direct = 0
		if (dx == block and dy == 0):
			self.direct = 1
		if (dx == -block and dy == 0):
			self.direct = 3
		x = (self.X + dx) // block
		y = (self.Y + dy) // block
		x = max(0, x)
		x = min(20, x)
		y = max(0, y)
		y = min(20, y)
		print(x, y)
		if (direct == self.direct and map[y][x] != "X" and map[y][x] != "#" and (x * block, y * block) != (enemy.X, enemy.Y)):
			self.X += dx
			self.Y += dy
			self.X = min(WIDTH - block, self.X)
			self.X = max(0, self.X)
			self.Y = min(HEIGHT - block, self.Y)
			self.Y = max(0, self.Y)

	def render(self):
		screen.blit(self.img[self.direct], (self.X, self.Y))
def gridRender():
	for i in range(block, WIDTH-block+1,block):
		pygame.draw.aaline(screen, WHITE , [i, 0], [i,HEIGHT] )
	for i in range(block, HEIGHT-block+1,block):
		pygame.draw.aaline(screen, WHITE , [0, i], [WIDTH, i] )	
class Box:
	def __init__(self, X, Y, type):
		self.X = X
		self.Y = Y
		self.type = type
		self.img = eval(type)
		self.hp = 1
		self.alive = True
	def destroy(self):
		if (self.type != "common"):
			return
		self.hp += 1
		if (self.hp >= 4):
			self.alive = False
		else:
			self.img = eval("common" + str(self.hp))
	def render(self):
		screen.blit(self.img, (self.X, self.Y))
def LoadMap():
	global boxes, map
	boxes = []
	f = open("map/map" + str(level), "r")
	map = f.read().split('\n')
	f.close()
	for i in range(len(map)):
		for j in range(len(map[i])):
			if (map[i][j] == '#'):
				boxes.append(Box(j * block, i * block, "common"))
			if (map[i][j] == 'X'):
				boxes.append(Box(j * block, i * block, "immortal"))
			if (map[i][j] == 'G'):
				boxes.append(Box(j * block, i * block, "ghost"))
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
hero = Tank (WIDTH-block, HEIGHT-block, [tankUP, tankRIGHT, tankDOWN, tankLEFT], 0)
enemy = Tank (0, 0, [enemyUP, enemyRIGHT, enemyDOWN, enemyLEFT], 2 )

boxes = []
map = []
LoadMap()



while(True):
	screen.fill(BLACK)
	pressed = pygame.key.get_pressed()
	for i in pygame.event.get():
		if (i.type == QUIT):
			pygame.quit()
		elif (i.type == KEYDOWN):
			if (i.key == K_ESCAPE):
				pygame.quit()
	if (pressed[K_LEFT] == 1):
		hero.move (-block, 0, enemy)
	elif (pressed[K_RIGHT] == 1):
		hero.move (block, 0, enemy)
	elif (pressed[K_UP] == 1):
		hero.move (0, -block, enemy)
	elif (pressed[K_DOWN] == 1):
		hero.move (0, block, enemy)	
	if (pressed[K_a] == 1):
		enemy.move (-block, 0, hero)
	elif (pressed[K_d] == 1):
		enemy.move (block, 0, hero)
	elif (pressed[K_w] == 1):
		enemy.move (0, -block, hero)
	elif (pressed[K_s] == 1):
		enemy.move (0, block, hero)		
	
		# 	print(chr(i.key))
	hero.render()
	enemy.render()	
	for i in boxes:
		i.render()
	gridRender()
	#pygame.draw.rect(screen, WHITE, (X, Y, 150, 75 ))
	pygame.display.update()	
	clock.tick(FPS)
