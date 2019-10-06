import settings
import random
class Box:
	def __init__(self, x, y, img):
		self.X = x
		self.Y = y
		self.img = img
		self.hp = 1
	def destroy(self):
		self.hp += 1
		if (self.hp == 4):
			return True
		self.img = eval("settings.box" + str(self.hp) + "Img")
		return False

def createBoxes():
	number = random.randint(70, 100)
	map = []
	boxes = []
	for i in range(number):
		x = random.randint(0, 11) * settings.block
		y = random.randint(0, 11) * settings.block
		while ((x, y) == (0, 0) or (x, y) == (550, 550) or (x,y) in map):
			x = random.randint(0, 11) * settings.block
			y = random.randint(0, 11) * settings.block
		map.append((x,y))
		boxes.append(Box(x, y, settings.box1Img))
	return boxes