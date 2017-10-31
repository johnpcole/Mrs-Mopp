import pygame








class Roomsizedefinition():
	
	def __init__(self):
		self.roomsize = Vectordefinition(36, 27)




class Messlibrary():
	
	def __init__(self):
		self.nomess =    -999
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
		self.bonustrigger = 200 #0
		self.refreshrate = 20
		

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
		self.healthboundary = [-999,             1,      50,   150,     850,     975,   1000]
		self.healthlabel =    ["Dead", "Exhausted", "Tired", "Fit", "Happy", "Drunk", "Dead"]
		self.healthfont =     [   1,            -1,       1,     0,       0,      -1,      1]
		
		self.clsprite = pygame.image.load("Confused_Right.png").convert()
		self.crsprite = pygame.image.load("Confused_Right.png").convert()



class Updatedictionary():
	
	def __init__(self, initialzone, initialstatus):
		self.tool =  initialzone
		self.status =  initialstatus



class Zonelibrary(Roomsizedefinition):
	
	def __init__(self):
		Roomsizedefinition.__init__(self)
		
		self.notool =   -999
		self.toolzone =   77
		self.cleanzone =  88
		self.helpzone =   99
		
		self.dustpan =     0
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
		self.status = -9999
		self.toolmode = initialtool
	
	def initialiseanimation(self, newtoolmode):
		self.status = self.start
		self.toolmode = newtoolmode
	
	def cleanspriteindex(self):
		animatehalf = self.start // 2
		animatestep = 1 + (animatehalf // 4)
		if self.status > animatehalf:
			outcome = (self.status - animatehalf) // animatestep
		else:
			outcome = self.status // animatestep
		return outcome
	
	def bonusspriteindex(self):
		clockvalue = (3 * self.length * self.status) // self.start
		if clockvalue > 20:
			outcome = clockvalue % 8
		else:
			outcome = 8 + (clockvalue % 2)
		return outcome
	
	def spellpositionindex(self):
		clockvalue = (3 * self.length * self.status) // self.start
		outcome = clockvalue % 28
		return outcome
	
	def animatespeed(self, refreshrate):
		outcome = self.start // (self.length * refreshrate)
		return outcome
	
	def timedecay(self, refreshrate, finishedstate):
		if self.toolmode != finishedstate:
			if self.status > -999:
				self.status = self.status - self.animatespeed(refreshrate)
			else:
				self.toolmode = finishedstate
	
	def killdecay(self):
		self.status = 0
	
	def stopanimation(self, finishedstate):
		self.toolmode = finishedstate
		self.status = -9999


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
