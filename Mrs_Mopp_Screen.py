import pygame
import Mrs_Mopp_Const


	def paint(self, window, icon, posx, posy):
		window.blit(icon,(posx * 20, posy * 20))



class Screensetup:
	
	def __init__(self, roomsize):
		self.spacing = 20
		self.size = Mrs_Mopp_Const.Vectordefinition()
		self.size = roomsize.factor(20)
	
	
	

		# for zonesearch in range(1, 10):
			# self.paint(window, self.sprite.tool[zonesearch], self.zonelocation.x[zonesearch], self.zonelocation.y[zonesearch])
		# pygame.display.flip()
	
	
	# def displaytool(self, window, changemode):
		# if changemode != 0:
			# if changemode > 0:
				# location = changemode
				# image = self.mess.emptysprite[changemode]
			# else:
				# location = 0 - changemode
				# image = 0 - changemode
			# self.paint(window, self.sprite.tool[image], self.zonelocation.x[location], self.zonelocation.y[location])
	
	
	
	# def displayclean(self, window, cleanmode, cleancount):
		# if cleanmode != self.piece.space:
			# currentzone = self.mess.cleanzone[cleanmode]
			# if cleancount <= 0:
				# self.paint(window, self.sprite.tool[currentzone], self.zonelocation.x[currentzone], self.zonelocation.y[currentzone])
			# else:
				# currentsprite = (cleancount // 51)
				# self.paint(window, self.sprite.cleanup[cleanmode][currentsprite], self.zonelocation.x[currentzone], self.zonelocation.y[currentzone])
	
	
	
