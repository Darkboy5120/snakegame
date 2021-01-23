import pygame, random

class Snake:
	def __init__(self, worldWidth, worldHeight, headStartPos):
		self.worldWidth, self.worldHeight = worldWidth, worldHeight
		self.headStartPos = headStartPos
		self.startDirection = 0
		self.headPos = None
		self.headLastPos = None
		self.direction = None
		self.cells = None
		self.reset()
	def grown(self):
		self.addCell(None, None)
	def setDirection(self, direction):
		oposite = self.direction+2
		if oposite>3: oposite = oposite-4
		if direction!=oposite and direction!=self.direction:
			self.direction = direction
	def move(self):
		self.headLastPos = self.headPos[:]
		if self.direction==0: self.headPos[0]+=1
		elif self.direction==1: self.headPos[1]-=1
		elif self.direction==2: self.headPos[0]-=1
		elif self.direction==3: self.headPos[1]+=1
		self.fixOverflow()
		self.updateCells()
	def fixOverflow(self):
		if self.headPos[0]==self.worldWidth: self.headPos[0] = 0
		elif self.headPos[0]<0: self.headPos[0] = self.worldWidth-1
		elif self.headPos[1]==self.worldHeight: self.headPos[1] = 0
		elif self.headPos[1]<0: self.headPos[1] = self.worldHeight-1
	def updateCells(self):
		previusLast = self.headLastPos
		currentPos = None
		for x in range(len(self.cells)):
			if x==0: self.cells[0] = self.headPos
			else:
				currentPos = self.cells[x]
				self.cells[x] = previusLast[:]
				previusLast = currentPos
	def reset(self):
		self.direction = self.startDirection
		self.headPos = self.headStartPos[:]
		self.cells = []
		self.addCell(self.headPos[0], self.headPos[1])
	def addCell(self, x, y):
		self.cells.append([x, y])
	def getInfo(self):
		return {"cells" : self.cells, "headLastPos" : self.headPos}

class World:
	def __init__(self, width, height, cellSize, emptyCellColor, snakeCellColor, foodColor):
		self.width, self.height = width, height
		self.cellSize = cellSize
		self.emptyCellColor = emptyCellColor
		self.snakeCellColor = snakeCellColor
		self.foodColor = foodColor
		self.cells = None
		self.food = None
		self.score = 0
		self.reset()
		self.putFood()
	def getScore(self):
		return self.score
	def snakeIsDead(self, cells, headLastPos):
		for x in range(len(cells)):
			if x==0: pass
			else:
				if headLastPos[0]==cells[x][0] and headLastPos[1]==cells[x][1]:
					return True
		return False
	def update(self, snakeInfo):
		cells, headLastPos = snakeInfo["cells"], snakeInfo["headLastPos"]
		self.reset()
		for x in range(len(cells)):
			self.cells[ cells[x][0] ][ cells[x][1] ] = 1
		if self.cells[ self.food[0] ][ self.food[1] ]==1:
			self.putFood()
			self.score+=1
			return 1
		elif self.snakeIsDead(cells, headLastPos):
			return 2
		else:
			self.cells[ self.food[0] ][ self.food[1] ] = 2
			return 0
	def putFood(self):
		done = False
		while not done:
			foodX = random.randint(0, self.width-1)
			foodY = random.randint(0, self.height-1)
			for x in range(self.width):
				if done: break
				for y in range(self.height):
					if foodX!=x and foodY!=y:
						if self.food==None or (foodX!=self.food[0] and foodY!=self.food[1]):
							done = True
							break
		self.food = [foodX, foodY]
	def reset(self):
		self.cells = [[0 for y in range(self.height)] for x in range(self.width)]
	def draw(self, surface):
		for x in range(self.width):
			for y in range(self.height):
				rectX = self.width+2+(self.cellSize*x)+(2*x)
				rectY = self.height+2+(self.cellSize*y)+(2*y)
				rect = pygame.rect.Rect(rectX, rectY, self.cellSize, self.cellSize)
				if self.cells[x][y]==0: color = self.emptyCellColor
				elif self.cells[x][y]==1: color = self.snakeCellColor
				elif self.cells[x][y]==2: color = self.foodColor
				pygame.draw.rect(surface, color, rect)

