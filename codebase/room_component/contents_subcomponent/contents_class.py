class ContentsClass:

	def __init__(self):

		self.contents = -999



	def set(self, newcontents):

		if newcontents == "Dust":
			self.contents = 1
		elif newcontents == "Mug":
			self.contents = 2
		elif newcontents == "Shirt":
			self.contents = 3
		elif newcontents == "Glass":
			self.contents = 4
		elif newcontents == "Pants":
			self.contents = 5
		elif newcontents == "Clean":
			self.contents = -999
		elif newcontents == "Spellcasting":
			self.contents = 77
		elif newcontents == "Wall":
			self.contents = 88
		elif newcontents == "Mrs Mopp":
			self.contents = 99
		else:
			print "Invalid Room Position Contents - ", newcontents
			x = 1/0



	def get(self):

		if self.contents == 1:
			outcome = "Dust"
		elif self.contents == 2:
			outcome = "Mug"
		elif self.contents == 3:
			outcome = "Shirt"
		elif self.contents == 4:
			outcome = "Glass"
		elif self.contents == 5:
			outcome = "Pants"
		elif self.contents == -999:
			outcome = "Clean"
		elif self.contents == 77:
			outcome = "Spellcasting"
		elif self.contents == 88:
			outcome = "Wall"
		elif self.contents == 88:
			outcome = "Mrs Mopp"
		else:
			print "Invalid Room Position Contents - ", self.contents
			outcome = 1/0
		return outcome



	def isclean(self):

		if self.contents == -999:
			outcome = True
		else:
			outcome = False
		return outcome



