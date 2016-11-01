import pygame

import code.definitions_component.definitions_class



#from Mrs_Mopp_Definitions import *



def operategame(mrsmopp, tools, event):
	if event.type == pygame.KEYDOWN:
		accelerate = 1
	elif event.type == pygame.KEYUP:
		accelerate = -1
	else:
		accelerate = 0
	if accelerate != 0:
		speedchange = code.definitions_component.definitions_class.Vectordefinition(0, 0)
		if event.key == pygame.K_LEFT:
			speedchange.x = 0 - accelerate
		elif event.key == pygame.K_RIGHT:
			speedchange.x = accelerate
		elif event.key == pygame.K_UP:
			speedchange.y = 0 - accelerate
		elif event.key == pygame.K_DOWN:
			speedchange.y = accelerate
		mrsmopp.changespeed(speedchange)
	if (accelerate == 1):
		if event.key == pygame.K_SPACE:
			tools.castspell()


def movemrsmopp(game, room, mrsmopp, tools):
	if mrsmopp.currentspeed() > 0:
		room.fillarea(room.space, mrsmopp.position, mrsmopp.moppsize)
		newposition = code.definitions_component.definitions_class.Vectordefinition(0, 0)
		newposition = mrsmopp.predictmove()
		collisions = room.collisiondetect(tools.currenttool, newposition, mrsmopp.moppsize)
		if tools.validatemove(collisions) == True:
			mrsmopp.move()
			tools.resetconfusion()
			if tools.currenttool != tools.notool:
				if collisions > 0:
					tools.fill(collisions)
					game.increasescore(10 * collisions)
			currentzone = tools.toolzonedetect(mrsmopp.position)
			if currentzone != tools.notool:
				game.increasescore(10 * tools.toolzoneaction(currentzone))
		room.fillarea(room.mrsmopp, mrsmopp.position, mrsmopp.moppsize)



def updategame(game, room, tools, mrsmopp):
	if game.levelup == True:
		game.newlevel()
	if game.bonusup == True:
		tools.createbonus()
		game.bonusup = False
	
	currentzone = tools.helpzonedetect(mrsmopp.position)
	if currentzone == tools.drink:
		mrsmopp.drink(game.refreshrate)
	elif currentzone == tools.bonus:
		tools.retrievebonus()
	
	if mrsmopp.determinehealth() == mrsmopp.dead:
		print("dead")
	
	tools.updatezones(game.refreshrate)
	#this bit is shite
	if tools.spellanimation.toolmode == tools.bonus:
		if tools.spellanimation.status == tools.spellanimation.start:
			room.fillareagap(room.spelling, mrsmopp.getspellposition(), mrsmopp.getspellsize())
		elif tools.spellanimation.status <= 0:
			room.fillarea(room.space, mrsmopp.getspellposition(), mrsmopp.getspellsize())
			tools.spellanimation.killdecay()
		tools.spellanimation.timedecay(game.refreshrate, tools.notool)
		print(tools.spellanimation.status)
	
	game.increasetime()



def createmess(game, room, mess):
	if mess.triggermess(game.level, game.time, game.refreshrate) == True:
		newposition = code.definitions_component.definitions_class.Vectordefinition(-999, -999)
		newposition = room.findspace()
		if newposition.x >= 0:
			mess.placemess(newposition)
			room.addmess(mess.newtype, mess.newposition)
		else:
			print("Cant create mess")



def preparegame(game, room, tools, window):
	room.buildroom()
	room.preparedisplay(window)
	tools.preparedisplay(window)
	pygame.display.flip()



def updatedisplay(mrsmopp, mess, tools, game, window):
	dressflashmode = False
	screenflashstatus = game.flashmode()
	if screenflashstatus == True:
		if tools.isfull(tools.currenttool) == True:
			dressflashmode = True
	mrsmopp.displaymrsmopp(tools.currenttool, dressflashmode, window)
	mrsmopp.displayconfusion(tools.confused, window)
	tools.displaytoolswap(window)
	tools.displayfulltools(screenflashstatus, window)
	tools.displaycleanup(game.refreshrate, window)
	tools.displaybonus(window)
	mess.displaymess(window)
	game.displayscore(window)
	game.displaylevel(window)
	game.displayhealth(window, mrsmopp.determinehealthlabel(), mrsmopp.determinehealthfont(), screenflashstatus)
	game.displayspells(window, tools.spells)
	pygame.display.flip()
	mrsmopp.erasemrsmopp(window)



class Gameclass(code.definitions_component.definitions_class.Gamelibrary):
	
	
	
	def __init__(self):
		code.definitions_component.definitions_class.Gamelibrary.__init__(self)
		self.level = 1
		self.score = 0
		self.displayedscore = -1
		self.time = 0
		self.levelup = False
		self.bonusup = False

	
	def resetgame(self):
		return 0
	
	def increasescore(self, amount):
		oldscore = self.score
		self.score = self.score + amount
		for trigger in self.leveltrigger:
			if oldscore < trigger:
				if self.score >= trigger:
					self.levelup = True
		oldscoreboundary = oldscore // self.bonustrigger
		newscoreboundary = self.score // self.bonustrigger
		if oldscoreboundary != newscoreboundary:
			self.bonusup = True
	
	def newlevel(self):
		self.level = self.level + 1
		self.levelup = False
	
	def increasetime(self):
		self.time = self.time + 1
		if self.time >= self.refreshrate * 10:
			self.time = 0
	
	def flashmode(self):
		clockvalue = 2 * self.time // self.refreshrate
		if clockvalue % 2 == 1:
			flashoutcome = True
		else:
			flashoutcome = False
		return flashoutcome
	
	def displayscore(self, window):
		if self.displayedscore < self.score:
			pygame.draw.rect(window, self.backgroundcolour, [self.scoreposition.x, self.scoreposition.y, 72, 20], 0)
			self.displayedscore = self.displayedscore + 1
			scorestring = "{:08}".format(self.displayedscore)
			scoretext = self.font.render(scorestring, True, self.fontcolour)
			window.blit(scoretext, (self.scoreposition.x, self.scoreposition.y))
			if self.displayedscore > 999999:
				overlaywidth = 1
			elif self.displayedscore > 99999:
				overlaywidth = 2
			elif self.displayedscore > 9999:
				overlaywidth = 3
			elif self.displayedscore > 999:
				overlaywidth = 4
			elif self.displayedscore > 99:
				overlaywidth = 5
			elif self.displayedscore > 9:
				overlaywidth = 6
			else:
				overlaywidth = 7
			pygame.draw.rect(window, self.backgroundcolour, [self.scoreposition.x, self.scoreposition.y, overlaywidth * 9, 20], 0)
	
	def displayhealth(self, window, healthlabel, healthfont, flashstatus):
		if healthfont == 0:
			healthfontcolour = self.fontcolour
		else:
			healthfontcolour = self.warningcolour
		pygame.draw.rect(window, self.backgroundcolour, [self.healthposition.x, self.healthposition.y, 100, 25], 0)
		if (healthfont >= 0) | (flashstatus == True):
			healthtext = self.font.render(healthlabel, True, healthfontcolour)
			window.blit(healthtext, (self.healthposition.x, self.healthposition.y))
		
	def displaylevel(self, window):
		pygame.draw.rect(window, self.backgroundcolour, [self.levelposition.x, self.levelposition.y, 100, 25], 0)
		leveltext = self.font.render("Level "+str(self.level), True, self.fontcolour)
		window.blit(leveltext, (self.levelposition.x, self.levelposition.y))
	
	def displayspells(self, window, spellcount):
		pygame.draw.rect(window, self.backgroundcolour, [self.spellposition.x, self.spellposition.y, 100, 25], 0)
		for index in range(1, 6):
			if spellcount >= index:
				window.blit(self.spritespell, (self.spellposition.x + (index * 10), self.spellposition.y))
