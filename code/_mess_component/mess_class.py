from messlibrary_subcomponent import MessLibraryClass

class MessClass():
	
	
	
	def __init__(self):
		self.newposition = code.definitions_component.definitions_class.Vectordefinition(self.nomess, self.nomess)
		self.newtype = self.nomess
	
	
	
	def triggermess(self, level, currenttime, refreshrate):
		outcome = False
		self.newtype = self.nomess
		for messsearch in self.item:
			if currenttime == self.trigger[messsearch] * refreshrate:
				if level >= self.level[messsearch]:
					self.newtype = messsearch
					outcome = True
		return outcome
	
	
	
	def placemess(self, messlocation):
		self.newposition = messlocation
	
	
	
	def displaymess(self, window):
		if self.newtype != self.nomess:
			paint(window, self.sprite[self.newtype], self.newposition.x, self.newposition.y)
			self.newtype = self.nomess
	
	
	
	def displayspell(self, window):
		if self.spellanimation.toolmode != self.notool:
			if self.spellanimation.status > 0:
				imageindex = self.bonusanimation.bonusspriteindex()
				#print(self.bonustimer, " ", imageindex)
				paint(window, self.spritebonus[imageindex], self.spritex[self.bonus], self.y[self.bonus])
			else:
				paint(window, self.sprite[self.emptyright], self.spritex[self.bonus], self.y[self.bonus])
				self.bonusanimation.stopanimation(self.notool)
