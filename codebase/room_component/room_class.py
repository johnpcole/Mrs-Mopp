import random
from ..common_components.vector_datatype import vector_module as Vector
from contents_subcomponent import contents_module as Contents



class DefineRoom:
	
	
	
	def __init__(self):
		self.roomsize = Vector.createfromvalues(36, 27)
		self.board = [[Contents.createcontents() for y in range(0, self.roomsize.gety() + 2)]
																			for x in range(0, self.roomsize.getx() + 2)]
		self.buildroom()

	
	
	def buildroom(self):

		sizex = self.roomsize.getx()
		sizey = self.roomsize.gety()

		for x in range(0, sizex + 2):
			for y in range(0, sizey + 2):
				self.setcontents(x, y, "Clean")
			for x in range(0, sizex + 2):
				self.setcontents(x, 0, "Wall")
				self.setcontents(x, sizey + 1, "Wall")

		for y in range(0, sizey + 2):
			for x in range(0, 3):
				self.setcontents(x, y, "Wall")
				self.setcontents(sizex + 1 - x, y, "Wall")
			if (y - 1) % 5 < 2:
				for x in range(0, 3):
					self.setcontents(1 + x, y, "Wall")
					self.setcontents(sizex - x, y, "Wall")



	def setcontents(self, positionx, positiony, newcontents):
		self.board[positionx][positiony].set(newcontents)



	def getcontents(self, positionx, positiony):
		return self.board[positionx][positiony].get()



	def isclean(self, positionx, positiony):
		return self.board[positionx][positiony].isclean()



#	def predictmove(self):
#		newposition = code.definitions_component.definitions_class.Vectordefinition(0, 0)
#		actualspeed = code.definitions_component.definitions_class.Vectordefinition(0, 0)
#		if self.determinehealth() == self.drunk:
#			actualspeed = scalevector(self.speed, -1)
#		else:
#			actualspeed = self.speed
#		newposition = sumvectors(self.position, actualspeed)
#		return newposition



	# def fillarea(self, outcome, topleftposition, areasize):
	# 	for xpos in range(topleftposition.x, topleftposition.x + areasize.x):
	# 		for ypos in range(topleftposition.y, topleftposition.y + areasize.y):
	# 			if self.board[xpos][ypos] != self.wall:
	# 				self.board[xpos][ypos] = outcome
	#
	#
	#
	# def fillareagap(self, outcome, topleftposition, areasize):
	# 	for xpos in range(topleftposition.x, topleftposition.x + areasize.x):
	# 		for ypos in range(topleftposition.y, topleftposition.y + areasize.y):
	# 			if self.board[xpos][ypos] == self.space:
	# 				self.board[xpos][ypos] = outcome
	#
	#
	#
	# def addmess(self, outcome, messlocation):
	# 	self.board[messlocation.x][messlocation.y] = outcome
	
	
	
#	def findspace(self):
#
#		maxattempts = 2 * self.roomsize.getarea()
#		attempts = 0
#		loopstatus = False
#		outcome = Vector.createfromvalues(-999, -999)
#		while loopstatus == False:
#			attemptx = random.randrange(5, self.roomsize.x - 3)
#			attempty = random.randrange(2, self.roomsize.y)
#			if self.isclean(attemptx, attempty) == True:
#				outcome = Vector.setfromvalues(attemptx, attempty)
#				loopstatus = True
#			else:
#				attempts = attempts + 1
#				if attempts > maxattempts:
#					loopstatus = True
#		return outcome
	
	
	
#	def collisiondetect(self, currenttool, topleftposition, areasize):
#
#		collisiontally = 0
#		for xpos in range(topleftposition.getx(), topleftposition.getx() + areasize.getx()):
#			for ypos in range(topleftposition.gety(), topleftposition.gety() + areasize.gety()):
#				if self.isclean(xpos, ypos) == False:
#					if self.getcontents(xpos, ypos) == currenttool:
#						collisiontally = collisiontally + 1
#					else:
#						collisiontally = collisiontally + 999
#		return collisiontally

	
	
	# def preparedisplay(self, window):
	# 	for x in range(0, self.roomsize.x + 2):
	# 		paint(window, self.sprite[self.wallfiller], x - 2, 0)
	# 		paint(window, self.sprite[self.wallfiller], x - 2, -1)
	# 		paint(window, self.sprite[self.wallfiller], x - 2, self.roomsize.y + 1)
	# 		paint(window, self.sprite[self.wallfiller], x - 2, self.roomsize.y + 2)
	#
	# 	for y in range(1, self.roomsize.y + 1):
	# 		paint(window, self.sprite[self.wallfiller], -1, y)
	# 		paint(window, self.sprite[self.wallfiller], self.roomsize.x - 1, y)
	#
	# 	for y in range(2, self.roomsize.y, 5):
	# 		paint(window, self.sprite[self.leftwall], 0, y)
	# 		paint(window, self.sprite[self.rightwall], self.roomsize.x - 2, y)
	#
	# 	paint(window, self.sprite[self.wallfiller], 0, 1)
	# 	paint(window, self.sprite[self.wallfiller], self.roomsize.x - 2, 1)
	# 	paint(window, self.sprite[self.wallfiller], 0, self.roomsize.y)
	# 	paint(window, self.sprite[self.wallfiller], self.roomsize.x - 2, self.roomsize.y)
