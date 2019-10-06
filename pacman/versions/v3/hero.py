class Hero:
	def __init__(self, X, Y, img):
		self.X = X
		self.Y = Y
		self.hp = 3
		self.img = img
		self.dx = 0
		self.dy = 0
	def move(self, dx, dy):
		self.X += dx
		self.Y += dy
