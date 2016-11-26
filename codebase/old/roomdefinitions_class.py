class RoomDefinitionClass(Roomsizedefinition):
	def __init__(self):
		Roomsizedefinition.__init__(self)
		self.space = -999
		self.dust = 0
		self.mug = 1
		self.shirt = 2
		self.glass = 3
		self.pants = 4
		self.spelling = 77
		self.wall = 88
		self.mrsmopp = 99

		self.leftwall = 0
		self.sprite = [pygame.image.load("Wall_Left.png").convert()]

		self.rightwall = 1
		self.sprite.append(pygame.image.load("Wall_Right.png").convert())

		self.wallfiller = 2
		self.sprite.append(pygame.image.load("Wall_Filler.png").convert())

