import code.definitions_component.definitions_class
from code.definitions_component.definitions_class import *

class PlayerClass(code.definitions_component.definitions_class.Mopplibrary):
	
	
	
	def __init__(self):
		code.definitions_component.definitions_class.Mopplibrary.__init__(self)
		self.moppsize = code.definitions_component.definitions_class.Vectordefinition(2, 3)
		self.health = 500
		self.speed = code.definitions_component.definitions_class.Vectordefinition(0, 0)
		self.position = code.definitions_component.definitions_class.Vectordefinition(5, 5)
	
	
	
	def changespeed(self, speeddelta):
		self.speed = sumvectors(self.speed, speeddelta)
	
	
	
	def currentspeed(self):
		outcome = vectorlength(self.speed)
		return outcome
	
	
	
	def getspellposition(self):
		newposition = code.definitions_component.definitions_class.Vectordefinition(-1, -1)
		newposition = sumvectors(newposition, self.position)
		return newposition
	
	
	
	def getspellsize(self):
		newposition = code.definitions_component.definitions_class.Vectordefinition(2, 2)
		newposition = sumvectors(newposition, self.moppsize)
		return newposition
	
	
	
	def predictmove(self):
		newposition = code.definitions_component.definitions_class.Vectordefinition(0, 0)
		actualspeed = code.definitions_component.definitions_class.Vectordefinition(0, 0)
		if self.determinehealth() == self.drunk:
			actualspeed = scalevector(self.speed, -1)
		else:
			actualspeed = self.speed
		newposition = sumvectors(self.position, actualspeed)
		return newposition
	
	
	
	def move(self):
		self.position = self.predictmove()
		self.health = self.health - 1
	
	
	
	def drink(self, refreshrate):
		self.health = self.health + (300 // refreshrate)
	
	
	
	def determinehealth(self):
		outcome = -999
		for index in self.healthindex:
			if self.health >= self.healthboundary[index]:
				outcome = self.healthmarker[index]
		return outcome
	
	
	
	def determinehealthlabel(self):
		outcome = self.healthlabel[1 + self.determinehealth()]
		return outcome
	
	
	
	def determinehealthfont(self):
		outcome = self.healthfont[1 + self.determinehealth()]
		return outcome
	
	
	
	def dressstatus(self, currenttool, flashmode):
		if currenttool == self.notool:
			dress = self.notooldress
		else:
			if flashmode == True:
				dress = self.fulltooldress
			else:
				dress = currenttool
		return dress
	
	
	def displayconfusion(self, confusionstatus, window):
		if confusionstatus == True:
			if self.position.x < 10:
				paint(window, self.clsprite, self.position.x, self.position.y)
			else:
				paint(window, self.crsprite, self.position.x, self.position.y)
	
	
	
	def displaymrsmopp(self, currenttool, flashmode, window):
		paint(window, self.spritedress[self.dressstatus(currenttool, flashmode)], self.position.x, self.position.y)
		paint(window, self.spritehead[self.determinehealth()], self.position.x, self.position.y)
	
	
	
	def erasemrsmopp(self, window):
		for xpos in range(self.position.x, self.position.x + self.moppsize.x):
			for ypos in range(self.position.y, self.position.y + self.moppsize.y):
				paint(window, self.spritespace, xpos, ypos)
