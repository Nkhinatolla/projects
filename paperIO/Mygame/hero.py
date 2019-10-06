class Hero:
	def __init__(self, X, Y, img):
		self.X = [X]
		self.Y = [Y]
		self.hp = 3
		self.img = img
		self.dx = 0
		self.dy = 20
	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy
	def update(self):
		x = self.X[-1] + self.dx
		y = self.Y[-1] + self.dy
		if (x >= 0 and x <=  and y >= 0 and y <= 600):
			self.X.append(x)
			self.Y.append(y)
	def render(self, screen):
		for i in range(len(self.X)):
			screen.blit(self.img, (self.X[i], self.Y[i]))
