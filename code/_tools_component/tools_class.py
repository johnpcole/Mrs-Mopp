from code.definitions_component import definitions_class
from code.definitions_component.definitions_class import *

class ToolClass(definitions_class.Zonelibrary):
	
	
	
	def __init__(self):
		definitions_class.Zonelibrary.__init__(self)
		self.currenttool = self.notool
		self.toolcapacity = 10
		self.cleananimation = definitions_class.Animatedefinition(2, self.notool)
		self.status = [0, 0, 0, 0, 0]
		self.updatetool = Updatedictionary(self.notool, self.notool)
		self.bonusanimation = definitions_class.Animatedefinition(30, self.notool)
		self.confused = False
		self.spells = 3
		self.spellanimation = definitions_class.Animatedefinition(10, self.notool)
	
	
	
	def checkcapacity(self, amounttoclean):
		if self.status[self.currenttool] + amounttoclean > self.toolcapacity:
			outcome = False
		else:
			outcome = True
		return outcome
	
	
	
	def isfull(self, tool):
		outcome = False
		if tool != self.notool:
			if self.status[tool] == self.toolcapacity:
				outcome = True
		return outcome
	
	
	
	def validatemove(self, collisiontally):
		validmove = False
		if self.currenttool == self.notool:
			if collisiontally == 0:
				validmove = True
		else:
			if self.checkcapacity(collisiontally) == True:
				validmove = True
		return validmove
	
	
	
	def fill(self, amounttoclean):
		self.status[self.currenttool] = self.status[self.currenttool] + amounttoclean
	
	
	
	def toolzonedetect(self, moppposition):
		outcome = self.notool
		for zonesearch in self.toolitem:
			if self.y[zonesearch] == moppposition.y:
				if self.moppx[zonesearch] == moppposition.x:
					outcome = zonesearch
		return outcome
	
	
	
	def toolzoneaction(self, zone):
		scoreupdate = 0
		if self.zonetype[zone] == self.toolzone:
			self.swaptool(zone)
		elif self.zonetype[zone] == self.cleanzone:
			scoreupdate = self.emptytool(zone)
		else:
			print("bonus or drink")
		return scoreupdate
	
	
	
	def swaptool(self, zone):
		errorswap = True
		if self.currenttool == self.notool:
			self.currenttool = zone
			self.updatetool.tool = zone
			self.updatetool.status = -1
			errorswap = False
		else:
			if zone == self.currenttool:
				self.currenttool = self.notool
				self.updatetool.tool = zone
				self.updatetool.status = 1
				errorswap = False
		self.confused = errorswap
	
	
	
	def emptytool(self, zone):
		errorempty = True
		scoreupdate = 0
		if self.currenttool != self.notool:
			if zone == self.cleanupzone[self.currenttool]:
				if self.status[self.currenttool] > 0:
					scoreupdate = self.status[self.currenttool]
					self.status[self.currenttool] = 0
					self.cleananimation.initialiseanimation(self.currenttool)
					errorempty = False
		self.confused = errorempty
		return scoreupdate
	
	
	
	def resetconfusion(self):
		self.confused = False
	
	
	
	def helpzonedetect(self, moppposition):
		outcome = self.notool
		for zonesearch in self.helpitem:
			if self.y[zonesearch] == moppposition.y:
				if self.moppx[zonesearch] == moppposition.x:
					outcome = zonesearch
		return outcome
	
	
	
	def createbonus(self):
		self.bonusanimation.initialiseanimation(self.bonus)
	
	
	
	def updatezones(self, refreshrate):
		self.cleananimation.timedecay(refreshrate, self.notool)
		self.bonusanimation.timedecay(refreshrate, self.notool)
	
	
	
	def retrievebonus(self):
		if self.bonusanimation.status > 0:
			self.spells = self.spells + 1
			self.bonusanimation.killdecay()
		else:
			self.confused = True
	
	
	
	def castspell(self):
		if self.spells > 0:
			if self.spellanimation.toolmode == self.notool:
				print("spell valid")
				self.spells = self.spells - 1
				self.spellanimation.initialiseanimation(self.bonus)
	
	
	
	def displaytoolswap(self, window):
		if self.updatetool.tool != self.notool:
			if self.updatetool.status > 0:
				imageindex = self.normalsprite[self.updatetool.tool]
			else:
				imageindex = self.emptysprite[self.updatetool.tool]
			paint(window, self.sprite[imageindex], self.spritex[self.updatetool.tool], self.y[self.updatetool.tool])
			self.updatetool.tool = self.notool
	
	
	
	def displayfulltools(self, flashmode, window):
			for tool in self.normalsprite:
				if tool != self.currenttool:
					if self.isfull(tool) == True:
						if flashmode == False:
							spriteindex = self.normalsprite[tool]
						else:
							spriteindex = self.fullsprite[tool]
						paint(window, self.sprite[spriteindex], self.spritex[tool], self.y[tool])
	
	
	
	def displaycleanup(self, refreshrate, window):
		if self.cleananimation.toolmode != self.notool:
			cleanzone = self.cleanupzone[self.cleananimation.toolmode]
			if self.cleananimation.status > 0:
				imageindexone = self.cleananimation.toolmode
				imageindextwo = self.cleananimation.cleanspriteindex()
				paint(window, self.spriteclean[imageindexone][imageindextwo], self.spritex[cleanzone], self.y[cleanzone])
			else:
				paint(window, self.sprite[cleanzone], self.spritex[cleanzone], self.y[cleanzone])
				self.cleananimation.stopanimation(self.notool)
	
	
	
	def displaybonus(self, window):
		if self.bonusanimation.toolmode != self.notool:
			if self.bonusanimation.status > 0:
				imageindex = self.bonusanimation.bonusspriteindex()
				#print(self.bonustimer, " ", imageindex)
				paint(window, self.spritebonus[imageindex], self.spritex[self.bonus], self.y[self.bonus])
			else:
				paint(window, self.sprite[self.emptyright], self.spritex[self.bonus], self.y[self.bonus])
				self.bonusanimation.stopanimation(self.notool)
	
	
	
	def preparedisplay(self, window):
		for zonesearch in self.item:
			if zonesearch != self.bonus:
				paint(window, self.sprite[zonesearch], self.spritex[zonesearch], self.y[zonesearch])
