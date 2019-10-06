import pygame, threading
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
			self.direct = 2 #down
		if (dx == 0 and dy == -block):
			self.direct = 0 #up
		if (dx == block and dy == 0):
			self.direct = 1 #right
		if (dx == -block and dy == 0):
			self.direct = 3 #left
		x = (self.X + dx) // block
		y = (self.Y + dy) // block	
		x = max(0, x)
		x = min(20, x)
		y = max(0, y)
		y = min(20, y)
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
	def	destroy(self):
		if (self.type != "common"): 
			return
		self.hp += 1
		if (self.hp >= 4):	
			self.alive = False
			x = self.X // block
			y = self.Y // block
			map[y] = map[y][:x] + '.' + map[y][x + 1:]
		else:
			self.img = eval("common" + str(self.hp))
	def render(self):
		screen.blit(self.img, (self.X, self.Y))
def LoadMap():	
	global boxes, map
	f = open("map/map" + str(level), "r")
	map = f.read().split("\n")
	f.close()
	for i in range(len(map)):
		for j in range(len(map[i])):
			if (map[i][j] == "#"):
				boxes.append(Box(j * block, i * block, "common"))
			if (map[i][j] == "X"):
				boxes.append(Box(j * block, i * block, "immortal"))
			if (map[i][j] == "G"):
				boxes.append(Box(j * block, i * block, "ghost"))	

class Bullet:
	def __init__(self, X, Y, radius, color, direct):
		self.X = X
		self.Y = Y
		self.radius = radius
		self.color = color
		self.direct = direct
		self.alive = True
		self.clock = pygame.time.Clock()
		self.thread = threading.Thread(target=self.move, args=[])
		self.thread.start()
	def move(self):
		while (self.alive == True):
			if (self.direct == 0):
				self.Y -= 5
			if (self.direct == 1):
				self.X += 5
			if (self.direct == 2):
				self.Y += 5
			if (self.direct == 3):
				self.X -= 5
			if (self.X >= WIDTH or self.X <= 0 or self.Y <= 0 or self.Y >= HEIGHT): # out of frame
				self.alive = False
			x = self.X // block
			y = self.Y // block
			for box in boxes:
				if ((box.X // block, box.Y // block) == (x, y)):
					if (box.type == "ghost"):
						break
					box.destroy()
					self.alive = False
					break
			self.clock.tick(60)
	def render(self):
		pygame.draw.circle(screen, self.color, (self.X, self.Y), self.radius)			
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
hero = Tank (WIDTH-block, HEIGHT-block, [tankUP, tankRIGHT, tankDOWN, tankLEFT], 0)
enemy = Tank (0, 0, [enemyUP, enemyRIGHT, enemyDOWN, enemyLEFT], 2 )

bullets = []

boxes = []
map = []
LoadMap()
boxes[0].destroy()


while(True):
	screen.fill(BLACK)
	pressed = pygame.key.get_pressed()
	for i in pygame.event.get():
		if (i.type == QUIT):
			pygame.quit()
		elif (i.type == KEYDOWN):
			if (i.key == K_ESCAPE):
				for i in bullets:
					i.alive = False
				pygame.quit()
			if (i.key == K_SPACE):
				bullets.append(Bullet(round(enemy.X + block // 2), round(enemy.Y + block // 2), 5, YELLOW, enemy.direct))
			if (i.key == K_l):
				bullets.append(Bullet(round(hero.X + block // 2), round(hero.Y + block // 2), 5, YELLOW, hero.direct))

	if (pressed[K_LEFT] == 1):
		hero.move (-block, 0 , enemy)
		# direct = 3
	elif (pressed[K_RIGHT] == 1):
		hero.move (block, 0, enemy)
		# direct = 1
	elif (pressed[K_UP] == 1):
		hero.move (0, -block, enemy)
		# direct = 0
	elif (pressed[K_DOWN] == 1):
		hero.move (0, block, enemy)	
		# direct = 2
	if (pressed[K_a] == 1):
		enemy.move (-block, 0, hero)
	elif (pressed[K_d] == 1):
		enemy.move (block, 0, hero)
	elif (pressed[K_w] == 1):
		enemy.move (0, -block, hero)
	elif (pressed[K_s] == 1):
		enemy.move (0, block, hero)		
	
		# 	print(chr(i.key))
	for i in bullets:
		if (i.alive == False):
			bullets.remove(i)
		else:
			i.render()
	hero.render()
	enemy.render()	
	gridRender()
	for i in boxes:
		if (i.alive == False):
			boxes.remove(i)
		else:
			i.render()
			
	#pygame.draw.rect(screen, WHITE, (X, Y, 150, 75 ))
	pygame.display.update()	
	clock.tick(FPS)
