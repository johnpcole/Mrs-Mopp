import Mrs_Mopp_Definitions
from Mrs_Mopp_Definitions import *

class Messclass(Mrs_Mopp_Definitions.Messlibrary):
	
	
	
	def __init__(self):
		Mrs_Mopp_Definitions.Messlibrary.__init__(self)
		self.newposition = Mrs_Mopp_Definitions.Vectordefinition(self.nomess, self.nomess)
		self.newtype = self.nomess
	
	
	
	def triggermess(self, level, currenttime, refreshrate):
		outcome = False
		self.newtype = self.nomess
		for messsearch in self.item:
			# if currenttime // refreshrate == currenttime / refreshrate:
			if currenttime == self.trigger[messsearch] * refreshrate:
				if level >= self.level[messsearch]:
					self.newtype = messsearch
					outcome = True
		return outcome
	
	
	
	def placemess(self, messlocation):
		self.newposition = messlocation
	
	
	
	def cancelmess(self):
		self.newtype = self.nomess
		print("Cant create mess")
	
	
	
	def displaymess(self, window):
		if self.newtype != self.nomess:
			paint(window, self.sprite[self.newtype], self.newposition.x, self.newposition.y)
			self.newtype = self.nomess
