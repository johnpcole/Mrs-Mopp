import Mrs_Mopp_Definitions
from Mrs_Mopp_Definitions import *

class Toolclass(Mrs_Mopp_Definitions.Zonelibrary):
	
	
	
	def __init__(self):
		Mrs_Mopp_Definitions.Zonelibrary.__init__(self)
		self.currenttool = self.notool
		self.toolcapacity = 10
		self.fillstatus = [0, 0, 0, 0, 0]
		self.sinkzone = Mrs_Mopp_Definitions.Animatedefinition(30, self.notool)
		self.washerzone = Mrs_Mopp_Definitions.Animatedefinition(30, self.notool)
		self.binzone = Mrs_Mopp_Definitions.Animatedefinition(30, self.notool)
		self.bonuszone = Mrs_Mopp_Definitions.Animatedefinition(30, self.notool)
		self.spells = 3
		self.spellaction = Mrs_Mopp_Definitions.Animatedefinition(5, self.notool)
		self.confused = Mrs_Mopp_Definitions.Animatedefinition(1, 0)
	
	
	
	def checkcapacity(self, amounttoclean):
		# Determines whether a move can be accomodated by the current tool
		# Pass in the amount of items to clean to get a true/false outcome
		if self.fillstatus[self.currenttool] + amounttoclean > self.toolcapacity:
			outcome = False
		else:
			outcome = True
		return outcome
	
	
	
	def isfull(self, tool):
		# Determines whether a specified tool is full
		# Pass in a tool to get a true/false outcome
		outcome = False
		if tool != self.notool:
			if self.fillstatus[tool] == self.toolcapacity:
				outcome = True
		return outcome
	
	
	
	def validatemove(self, collisiontally):
		# Determines whether a move can be made based on current tool
		# Pass in the amount of items to clean to get true/false outcome
		validmove = False
		if self.currenttool == self.notool:
			if collisiontally == 0:
				validmove = True
		else:
			if self.checkcapacity(collisiontally) == True:
				validmove = True
		return validmove
	
	
	
	def fill(self, amounttoclean):
		# Updates current tool fill value
		# Pass in the amount of items to clean
		self.fillstatus[self.currenttool] = self.fillstatus[self.currenttool] + amounttoclean
	
	
	
	def toolzonedetect(self, moppposition):
		# Determines whether player is positioned in a tool zone
		# Pass in player position vector to get tool zone enumerator outcome
		outcome = self.notool
		for zonesearch in self.toolitem:
			if self.y[zonesearch] == moppposition.y:
				if self.moppx[zonesearch] == moppposition.x:
					outcome = zonesearch
		return outcome
	
	
	
	def toolzoneaction(self, zone):
		# Invokes the appropriate tool zone action (swap tool or empty tool)
		# Pass in tool zone enumeration to get additional score outcome
		scoreupdate = 0
		if self.zonetype[zone] == self.toolzone:
			self.swaptool(zone)
		elif self.zonetype[zone] == self.cleanzone:
			scoreupdate = self.emptytool(zone)
		else:
			print("bonus or drink")
		return scoreupdate
	
	
	
	def swaptool(self, zone):
		# Swaps the current tool (picks up or drops)
		# Pass in tool zone enumeration
		errorswap = True
		if self.currenttool == self.notool:
			self.currenttool = zone
			errorswap = False
		else:
			if zone == self.currenttool:
				self.currenttool = self.notool
				errorswap = False
		if errorswap == True:
			self.confused.initialise(1)
	
	
	
	def emptytool(self, zone):
		# Empties the current tool
		# Pass in tool zone enumeration to get additional score outcome
		errorempty = True
		scoreupdate = 0
		if self.currenttool != self.notool:
			if zone == self.cleanupzone[self.currenttool]:
				if self.fillstatus[self.currenttool] > 0:
					if self.invokecleanzone(zone) == True:
						scoreupdate = self.fillstatus[self.currenttool]
						self.fillstatus[self.currenttool] = 0
						errorempty = False
		if errorempty == True:
			self.confused.initialise(1)
		return scoreupdate
	
	
	
	def invokecleanzone(self, zone):
		# Determines whether the specified zone is still in the process of cleaning
		# If not in use, starts a new clean cycle
		# Pass in the tool zone enumeration to get true/false outcome
		outcome = False
		if zone == self.washer:
			statusvalue = self.washerzone.counter
		elif zone == self.sink:
			statusvalue = self.sinkzone.counter
		elif zone == self.bin:
			statusvalue = self.binzone.counter
		else:
			statusvalue = -999
		if statusvalue <= 0:
			outcome = True
			if zone == self.washer:
				self.washerzone.initialise(self.currenttool)
			elif zone == self.sink:
				self.sinkzone.initialise(self.currenttool)
			elif zone == self.bin:
				self.binzone.initialise(self.currenttool)
		return outcome
	
	
	
	def resetconfusion(self):
		# Resets the current confused status
		self.confused.reset(0)
	
	
	
	def helpzonedetect(self, moppposition):
		# Determines whether player is positioned in a help zone
		# Pass in player position vector to get help zone enumerator outcome
		outcome = self.notool
		for zonesearch in self.helpitem:
			if self.y[zonesearch] == moppposition.y:
				if self.moppx[zonesearch] == moppposition.x:
					outcome = zonesearch
		return outcome
	
	
	
	def createbonus(self):
		self.bonuszone.initialise(self.bonus)
	
	
	
	def updatezones(self, refreshrate):
		self.washerzone.decay(refreshrate, self.notool)
		self.sinkzone.decay(refreshrate, self.notool)
		self.binzone.decay(refreshrate, self.notool)
		self.bonuszone.decay(refreshrate, self.notool)
		self.confused.decay(refreshrate, 0)
	
	
	
	def retrievebonus(self):
		if self.bonuszone.status != self.notool:
			self.spells = self.spells + 1
			self.bonuszone.reset(self.notool)
#		else:
#			self.confused.initialise(1)
	
	
	
	def castspell(self):
#		outcome = False
		if self.spells > 0:
			if self.spellaction.status == self.notool:
				self.spells = self.spells - 1
				self.spellaction.initialise(self.bonus)
#				outcome = True
#		return outcome
	
	
	
	def updatespell(self, refreshrate):
		oldstatus = self.spellaction.status
		self.spellaction.decay(refreshrate, self.notool)
		if oldstatus == self.spellaction.status:
			outcome = False
		else:
			outcome = True
		return outcome
	
	
	
	def displaytools(self, flashmode, window):
		for tool in self.normalsprite:
			if tool == self.currenttool:
				spriteindex = self.emptysprite[tool]
			else:
				spriteindex = self.normalsprite[tool]
				if self.isfull(tool) == True:
					if flashmode == True:
						spriteindex = self.fullsprite[tool]
			paint(window, self.sprite[spriteindex], self.spritex[tool], self.y[tool])
	
	
	
	def displaysink(self, window):
		spritepos = Mrs_Mopp_Definitions.Vectordefinition(self.spritex[self.sink], self.y[self.sink])
		if self.sinkzone.status != self.notool:
			imageindexone = self.sinkzone.status
			imageindextwo = self.sinkzone.cleanspriteindex()
			paint(window, self.spriteclean[imageindexone][imageindextwo], spritepos.x, spritepos.y)
		else:
			paint(window, self.sprite[self.sink], spritepos.x, spritepos.y)
	
	
	
	def displaywasher(self, window):
		spritepos = Mrs_Mopp_Definitions.Vectordefinition(self.spritex[self.washer], self.y[self.washer])
		if self.washerzone.status != self.notool:
			imageindexone = self.washerzone.status
			imageindextwo = self.washerzone.cleanspriteindex()
			paint(window, self.spriteclean[imageindexone][imageindextwo], spritepos.x, spritepos.y)
		else:
			paint(window, self.sprite[self.washer], spritepos.x, spritepos.y)
	
	
	
	def displaybin(self, window):
		spritepos = Mrs_Mopp_Definitions.Vectordefinition(self.spritex[self.bin], self.y[self.bin])
		if self.binzone.status != self.notool:
			imageindexone = self.binzone.status
			imageindextwo = self.binzone.cleanspriteindex()
			paint(window, self.spriteclean[imageindexone][imageindextwo], spritepos.x, spritepos.y)
		else:
			paint(window, self.sprite[self.bin], spritepos.x, spritepos.y)
	
	
	
	def displaybonus(self, window):
		spritepos = Mrs_Mopp_Definitions.Vectordefinition(self.spritex[self.bonus], self.y[self.bonus])
		if self.bonuszone.status != self.notool:
			imageindex = self.bonuszone.bonusspriteindex()
			paint(window, self.spritebonus[imageindex], spritepos.x, spritepos.y)
		else:
			paint(window, self.sprite[self.emptyright], spritepos.x, spritepos.y)
	
	
	
	def preparedisplay(self, window):
		for zonesearch in self.item:
			if zonesearch != self.bonus:
				paint(window, self.sprite[zonesearch], self.spritex[zonesearch], self.y[zonesearch])
