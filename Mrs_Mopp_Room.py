import Mrs_Mopp_Definitions
from Mrs_Mopp_Definitions import *
import random

class Roomclass(Mrs_Mopp_Definitions.Roomlibrary):
	
	
	
	def __init__(self):
		Mrs_Mopp_Definitions.Roomlibrary.__init__(self)
		self.board = [[self.space for y in range(0, self.roomsize.y + 2)] for x in range(0, self.roomsize.x + 2)]
	
	
	
	def buildroom(self):
		for x in range(0, self.roomsize.x + 2):
			for y in range(0, self.roomsize.y + 2):
				self.board[x][y] = self.space
			self.board[x][0] = self.wall
			self.board[x][self.roomsize.y + 1] = self.wall
		for y in range(0, self.roomsize.y + 2):
			for x in range (0, 3):
				self.board[x][y] = self.wall
				self.board[self.roomsize.x + 1 - x][y] = self.wall
			if (y - 1) % 5 < 2:
				for x in range(0, 3):
					self.board[1 + x][y] = self.wall
					self.board[self.roomsize.x - x][y] = self.wall
	
	
	
	def fillarea(self, outcome, topleftposition, areasize):
		for xpos in range(topleftposition.x, topleftposition.x + areasize.x):
			for ypos in range(topleftposition.y, topleftposition.y + areasize.y):
				if self.board[xpos][ypos] != self.wall:
					self.board[xpos][ypos] = outcome
	
	
	
	def addmess(self, outcome, messlocation):
		self.board[messlocation.x][messlocation.y] = outcome
	
	
	
	def findspace(self):
		attempts = 0
		loopstatus = False
		attempt = Mrs_Mopp_Definitions.Vectordefinition(-999, -999)
		outcome = Mrs_Mopp_Definitions.Vectordefinition(-999, -999)
		while loopstatus == False:
			attempt.x = random.randrange(5, self.roomsize.x - 3)
			attempt.y = random.randrange(2, self.roomsize.y)
			if self.board[attempt.x][attempt.y] == self.space:
				outcome = attempt
				loopstatus = True
			else:
				attempts = attempts + 1
				if attempts > vectorarea(self.roomsize):
					loopstatus = True
		return outcome
	
	
	
	def collisiondetect(self, currenttool, topleftposition, areasize):
		collisiontally = 0
		for xpos in range(topleftposition.x, topleftposition.x + areasize.x):
			for ypos in range(topleftposition.y, topleftposition.y + areasize.y):
				if self.board[xpos][ypos] != self.space:
					if self.board[xpos][ypos] == currenttool:
						collisiontally = collisiontally + 1
					else:
						collisiontally = collisiontally + 9999
		return collisiontally
	
	
	
	def displayspell(self, window, topleftposition, spellinfo):
		if spellinfo.counter > 0:
			for z in range(0, 4):
				locationindex = spellinfo.spellpositionindex(z)
				if z == 0:
					imageindex = self.spellstar + (locationindex % 2)
				elif z == 3:
					imageindex = self.emptyspace
				else:
					imageindex = self.spellstar + (self.trailtype[locationindex]) + (z - 1)
				starposition = Mrs_Mopp_Definitions.Vectordefinition(self.starposx[locationindex], self.starposy[locationindex])
				starposition = sumvectors(starposition, topleftposition)
				if self.board[starposition.x][starposition.y] == self.spelling:
					paint(window, self.sprite[imageindex], starposition.x, starposition.y)
	
	
	
	def erasespell(self, window, topleftposition, spellinfo):
		if spellinfo.counter > 0:
			for z in range(0, 3):
				locationindex = spellinfo.spellpositionindex(z)
				starposition = Mrs_Mopp_Definitions.Vectordefinition(self.starposx[locationindex], self.starposy[locationindex])
				starposition = sumvectors(starposition, topleftposition)
				if self.board[starposition.x][starposition.y] == self.spelling:
					paint(window, self.sprite[self.emptyspace], starposition.x, starposition.y)
	
	
	
	def preparedisplay(self, window):
		for x in range(0, self.roomsize.x + 2):
			paint(window, self.sprite[self.wallfiller], x - 2, 0)
			paint(window, self.sprite[self.wallfiller], x - 2, -1)
			paint(window, self.sprite[self.wallfiller], x - 2, self.roomsize.y + 1)
			paint(window, self.sprite[self.wallfiller], x - 2, self.roomsize.y + 2)
		
		for y in range(1, self.roomsize.y + 1):
			paint(window, self.sprite[self.wallfiller], -1, y)
			paint(window, self.sprite[self.wallfiller], self.roomsize.x - 1, y)
		
		for y in range(2, self.roomsize.y, 5):
			paint(window, self.sprite[self.leftwall], 0, y)
			paint(window, self.sprite[self.rightwall], self.roomsize.x - 2, y)
		
		paint(window, self.sprite[self.wallfiller], 0, 1)
		paint(window, self.sprite[self.wallfiller], self.roomsize.x - 2, 1)
		paint(window, self.sprite[self.wallfiller], 0, self.roomsize.y)
		paint(window, self.sprite[self.wallfiller], self.roomsize.x - 2, self.roomsize.y)
