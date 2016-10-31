import pygame



class Vectordefinition():
	
	def __init__(self, xval, yval):
		self.x = xval
		self.y = yval



def vectorarea(vector):
	outcome = vector.x * vector.y
	return outcome



def sumvectors(first, second):
	outcome = Vectordefinition(0, 0)
	outcome.x = first.x + second.x
	outcome.y = first.y + second.y
	return outcome



def scalevector(vector, factor):
	outcome = Vectordefinition(0, 0)
	outcome.x = vector.x * factor
	outcome.y = vector.y * factor
	return outcome



def vectorlength(vector):
	outcome = vector.x ** 2
	outcome = outcome + (vector.y ** 2)
	outcome = outcome ** 0.5
	return outcome



class Roomsizedefinition():
	
	def __init__(self):
		self.roomsize = Vectordefinition(36, 27)



class Roomlibrary(Roomsizedefinition):
	
	def __init__(self):
		Roomsizedefinition.__init__(self)
		self.space =  -999
		self.dust =      0
		self.mug =       1
		self.shirt =     2
		self.glass =     3
		self.pants =     4
		self.spelling = 77
		self.wall =     88
		self.mrsmopp =  99
		
		self.leftwall =   0
		self.sprite =     [pygame.image.load("Wall_Left.png").convert()]
		
		self.rightwall =  1
		self.sprite.append(pygame.image.load("Wall_Right.png").convert())
		
		self.wallfiller = 2
		self.sprite.append(pygame.image.load("Wall_Filler.png").convert())
		
		self.emptyspace = 3
		self.sprite.append(pygame.image.load("Space.png").convert())
		
		self.spellstar = 4
		self.sprite.append(pygame.image.load("Star_0.png").convert())
		self.sprite.append(pygame.image.load("Star_1.png").convert())
		self.sprite.append(pygame.image.load("Trail_TL.png").convert())
		self.sprite.append(pygame.image.load("End_TL.png").convert())
		self.sprite.append(pygame.image.load("Trail_L.png").convert())
		self.sprite.append(pygame.image.load("End_L.png").convert())
		self.sprite.append(pygame.image.load("Trail_BL.png").convert())
		self.sprite.append(pygame.image.load("End_BL.png").convert())
		self.sprite.append(pygame.image.load("Trail_B.png").convert())
		self.sprite.append(pygame.image.load("End_B.png").convert())
		self.sprite.append(pygame.image.load("Trail_BR.png").convert())
		self.sprite.append(pygame.image.load("End_BR.png").convert())
		self.sprite.append(pygame.image.load("Trail_R.png").convert())
		self.sprite.append(pygame.image.load("End_R.png").convert())
		self.sprite.append(pygame.image.load("Trail_TR.png").convert())
		self.sprite.append(pygame.image.load("End_TR.png").convert())
		self.sprite.append(pygame.image.load("Trail_T.png").convert())
		self.sprite.append(pygame.image.load("End_T.png").convert())
		
		self.starposx =  [ 0,  0,  0,  0,  0,  1,  2,  3,  3,  3,  3,  3,  2,  1]
		self.starposy =  [ 0,  1,  2,  3,  4,  4,  4,  4,  3,  2,  1,  0,  0,  0]
		self.trailtype = [ 2,  4,  4,  4,  6,  8,  8, 10, 12, 12, 12, 14, 16, 16]



class Messlibrary():
	
	def __init__(self):
		self.nomess =    -999
		
		self.newdust =      0
		self.sprite =     [pygame.image.load("Mess_Dust.png").convert()]
		
		self.newmug =       1
		self.sprite.append(pygame.image.load("Mess_Mug.png").convert())
		
		self.newshirt =     2
		self.sprite.append(pygame.image.load("Mess_Shirt.png").convert())
		
		self.newglass =     3
		self.sprite.append(pygame.image.load("Mess_Glass.png").convert())
		
		self.newpants =     4
		self.sprite.append(pygame.image.load("Mess_Pants.png").convert())
		
		self.item =    [0, 1, 2, 3, 4]
		self.trigger = [7, 4, 5, 6, 8]
		self.level =   [1, 1, 2, 3, 4]



class Gamelibrary():
	
	def __init__(self):
		self.leveltrigger = [500, 1500, 3000]
		self.bonustrigger = 5000
		self.refreshrate = 25
		
		self.font = pygame.font.Font("Mrs_Mopp.ttf", 18)
		self.backgroundcolour = [153, 153, 153]
		self.fontcolour = [0, 0, 0]
		self.warningcolour = [230, 25, 25]
		
		self.scoreposition = Vectordefinition(690, 10)
		self.healthposition = Vectordefinition(450, 10)
		self.levelposition = Vectordefinition(35, 10)
		self.spellposition = Vectordefinition(220, 9)
		
		self.spritespell = pygame.image.load("Spell.png").convert()



class Mopplibrary():
	
	def __init__(self):
		
		self.spritespace = pygame.image.load("Mess_Space.png").convert()
		
		self.dustpan =     0
		self.spritedress =     [pygame.image.load("MrsMopp_D.png").convert()]
		
		self.mugtray =     1
		self.spritedress.append(pygame.image.load("MrsMopp_M.png").convert())
		
		self.shirtbasket = 2
		self.spritedress.append(pygame.image.load("MrsMopp_S.png").convert())
		
		self.glasstray =   3
		self.spritedress.append(pygame.image.load("MrsMopp_G.png").convert())
		
		self.pantsbasket = 4
		self.spritedress.append(pygame.image.load("MrsMopp_P.png").convert())
		
		self.notool =    -999
		self.notooldress =    5
		self.spritedress.append(pygame.image.load("MrsMopp_N.png").convert())
		
		self.fulltooldress =  6
		self.spritedress.append(pygame.image.load("MrsMopp_F.png").convert())
		
		self.exhausted =   0
		self.spritehead =     [pygame.image.load("MrsMopp_0.png").convert()]
		
		self.tired =       1
		self.spritehead.append(pygame.image.load("MrsMopp_1.png").convert())
		
		self.fit =         2
		self.spritehead.append(pygame.image.load("MrsMopp_2.png").convert())
		
		self.happy =       3
		self.spritehead.append(pygame.image.load("MrsMopp_3.png").convert())
		
		self.drunk =       4
		self.spritehead.append(pygame.image.load("MrsMopp_4.png").convert())
		
		self.dead =       -1
		self.healthindex =    [   0,             1,       2,     3,       4,       5,      6]
		self.healthmarker =   [  -1,             0,       1,     2,       3,       4,     -1]
		self.healthboundary = [-999,             1,     100,   300,    1700,    1950,   2000]
		self.healthlabel =    ["Dead", "Exhausted", "Tired", "Fit", "Happy", "Drunk", "Dead"]
		self.healthfont =     [   1,            -1,       1,     0,       0,      -1,      1]
		
		self.confusedleftsprite = pygame.image.load("Confused_Left.gif").convert()
		self.confusedrightsprite = pygame.image.load("Confused_Right.gif").convert()



class Zonelibrary(Roomsizedefinition):
	
	def __init__(self):
		Roomsizedefinition.__init__(self)
		
		self.notool =   -999
		self.toolzone =   77
		self.cleanzone =  88
		self.helpzone =   99
		
		self.dustpan =       0
		self.sprite =     [pygame.image.load("Tool_Dustpan_Dust.png").convert()]
		
		self.mugtray =       1
		self.sprite.append(pygame.image.load("Tool_Tray_Mug.png").convert())
		
		self.shirtbasket =   2
		self.sprite.append(pygame.image.load("Tool_Basket_Shirt.png").convert())
		
		self.glasstray =     3
		self.sprite.append(pygame.image.load("Tool_Tray_Glass.png").convert())
		
		self.pantsbasket =   4
		self.sprite.append(pygame.image.load("Tool_Basket_Pants.png").convert())
		
		self.washer =        5
		self.sprite.append(pygame.image.load("Washer.png").convert())
		
		self.sink =          6
		self.sprite.append(pygame.image.load("Sink.png").convert())
		
		self.bin =           7
		self.sprite.append(pygame.image.load("Bin.png").convert())
		
		self.drink =         8
		self.sprite.append(pygame.image.load("Tool_Empty_Left.png").convert()) # Drink
		
		self.bonus =         9
		self.sprite.append(pygame.image.load("Tool_Empty_Right.png").convert()) # Bonus Spell
		
		self.emptyleft =       10
		self.sprite.append(pygame.image.load("Tool_Empty_Left.png").convert())
		
		self.emptyright =       11
		self.sprite.append(pygame.image.load("Tool_Empty_Right.png").convert())
		
		self.fulldustpan =  12
		self.sprite.append(pygame.image.load("Tool_Dustpan_Full.png").convert())
		
		self.fulltray =     13
		self.sprite.append(pygame.image.load("Tool_Tray_Full.png").convert())
		
		self.fullbasket =   14
		self.sprite.append(pygame.image.load("Tool_Basket_Full.png").convert())
		
		self.item =         [ 0,  1,                 2,  3,                 4,  5,                 6,                 7,  8,                 9 ]
		self.toolitem =     [ 0,  1,                 2,  3,                 4,  5,                 6,                 7                        ]
		self.helpitem =     [                                                                                             8,                 9 ]
		self.moppx =        [ 3,  3, self.roomsize.x-3,  3, self.roomsize.x-3,  3, self.roomsize.x-3, self.roomsize.x-3,  3, self.roomsize.x-3 ]
		self.spritex =      [ 0,  0, self.roomsize.x-1,  0, self.roomsize.x-1,  0, self.roomsize.x-1, self.roomsize.x-1,  0, self.roomsize.x-1 ]
		self.y =            [13, 23,                 3,  3,                23, 18,                 8,                18,  8,                13 ]
		self.zonetype =     [self.toolzone, self.toolzone, self.toolzone, self.toolzone, self.toolzone, self.cleanzone, self.cleanzone, self.cleanzone, self.helpzone, self.helpzone]
		self.cleanupzone =  [self.bin,           self.sink,          self.washer,        self.sink,          self.washer         ]
		self.normalsprite = [self.dustpan,       self.mugtray,       self.shirtbasket,   self.glasstray,     self.pantsbasket    ]
		self.emptysprite =  [self.emptyleft,     self.emptyleft,     self.emptyright,    self.emptyleft,     self.emptyright     ]
		self.fullsprite =   [self.fulldustpan,   self.fulltray,      self.fullbasket,    self.fulltray,      self.fullbasket     ]
		
		self.spriteclean = []
		self.spriteclean.append([])
		self.spriteclean[0].append(pygame.image.load("Bin_D0.png").convert())
		self.spriteclean[0].append(pygame.image.load("Bin_D1.png").convert())
		self.spriteclean[0].append(pygame.image.load("Bin_D2.png").convert())
		self.spriteclean[0].append(pygame.image.load("Bin_D3.png").convert())
		self.spriteclean.append([])
		self.spriteclean[1].append(pygame.image.load("Sink_M0.png").convert())
		self.spriteclean[1].append(pygame.image.load("Sink_M1.png").convert())
		self.spriteclean[1].append(pygame.image.load("Sink_M2.png").convert())
		self.spriteclean[1].append(pygame.image.load("Sink_M3.png").convert())
		self.spriteclean.append([])
		self.spriteclean[2].append(pygame.image.load("Washer_S0.png").convert())
		self.spriteclean[2].append(pygame.image.load("Washer_S1.png").convert())
		self.spriteclean[2].append(pygame.image.load("Washer_S2.png").convert())
		self.spriteclean[2].append(pygame.image.load("Washer_S3.png").convert())
		self.spriteclean.append([])
		self.spriteclean[3].append(pygame.image.load("Sink_G0.png").convert())
		self.spriteclean[3].append(pygame.image.load("Sink_G1.png").convert())
		self.spriteclean[3].append(pygame.image.load("Sink_G2.png").convert())
		self.spriteclean[3].append(pygame.image.load("Sink_G3.png").convert())
		self.spriteclean.append([])
		self.spriteclean[4].append(pygame.image.load("Washer_P0.png").convert())
		self.spriteclean[4].append(pygame.image.load("Washer_P1.png").convert())
		self.spriteclean[4].append(pygame.image.load("Washer_P2.png").convert())
		self.spriteclean[4].append(pygame.image.load("Washer_P3.png").convert())
		
		self.spritebonus =     [pygame.image.load("Bonus_A0.png").convert()]
		self.spritebonus.append(pygame.image.load("Bonus_A1.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A2.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A3.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A4.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A5.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A6.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_A7.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_B0.png").convert())
		self.spritebonus.append(pygame.image.load("Bonus_B1.png").convert())



class Animatedefinition():
	
	def __init__(self, animationlength, initialtool):
		self.length = animationlength
		self.start = 10000
		self.counter = -9999
		self.status = initialtool
	
	def initialise(self, newstatusmode):
		self.counter = self.start
		self.status = newstatusmode
	
	def cleanspriteindex(self):
		outcome = (self.counter // 100) % 4
		return outcome
	
	def bonusspriteindex(self):
		clockvalue = self.counter // 100
		if clockvalue > 20:
			outcome = clockvalue % 8
		else:
			outcome = 8 + (clockvalue % 2)
		return outcome
	
	def spellpositionindex(self, offset):
		clockvalue = (self.counter // 150) + offset
		outcome = clockvalue % 14
		return outcome
	
	def decayspeed(self, refreshrate):
		outcome = self.start // (self.length * refreshrate)
		return outcome
	
	def decay(self, refreshrate, finishedstate):
		if self.counter < 0:
			self.status = finishedstate
		else:
			self.counter = self.counter - self.decayspeed(refreshrate)
	
	def reset(self, finishedstate):
		self.status = finishedstate
		self.counter = -9999


def preparewindow():
	roomsize = Roomsizedefinition()
	screensize = Vectordefinition(4, 3)
	screensize = sumvectors(roomsize.roomsize, screensize)
	screensize = scalevector(screensize, 20)
	window = pygame.display.set_mode((screensize.x, screensize.y))
	pygame.display.set_caption("Mrs. Mopp")
	return window



def paint(window, icon, posx, posy):
	window.blit(icon, ((1 + posx) * 20, (1 + posy) * 20))
