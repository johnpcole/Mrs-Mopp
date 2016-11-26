class DefineVector:

	def __init__(self):
		self.x = 0
		self.y = 0



	def setx(self, xval):
		self.x = xval



	def sety(self, yval):
		self.y = yval



	def setfromvalues(self, xval, yval):
		self.x = xval
		self.y = yval



	def setfromobject(self, vectorobject):
		self.x = vectorobject.x
		self.y = vectorobject.y



	def adjust(self, vectorobject):
		self.x = self.x + vectorobject.x
		self.y = self.y + vectorobject.y



	def getx(self):
		return self.x



	def gety(self):
		return self.y



	def getcoordinates(self):
		return self.x, self.y



	def getarea(self):
		return self.x * self.y



	def getscaled(self, factor):
		outcome = DefineVector()
		outcome.x = self.x * factor
		outcome.y = self.y * factor
		return outcome



	def getlength(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5
