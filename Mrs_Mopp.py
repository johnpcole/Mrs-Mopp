import pygame
import Mrs_Mopp_Definitions

pygame.init()
clock = pygame.time.Clock()
window = Mrs_Mopp_Definitions.preparewindow()

import Mrs_Mopp_Player
import Mrs_Mopp_Room
import Mrs_Mopp_Mess
import Mrs_Mopp_Tools
import Mrs_Mopp_Game

room = Mrs_Mopp_Room.Roomclass()
mrsmopp = Mrs_Mopp_Player.Mrsmoppclass()
mess = Mrs_Mopp_Mess.Messclass()
tools = Mrs_Mopp_Tools.Toolclass()
game = Mrs_Mopp_Game.Gameclass()

Mrs_Mopp_Game.preparegame(game, room, tools, mrsmopp, window)

quitscreen = False
while quitscreen == False:

	# EVENT PROCESSING
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitscreen = True
		else:
			Mrs_Mopp_Game.operategame(mrsmopp, tools, event)
	
	# GAME LOGIC
	
	Mrs_Mopp_Game.movemrsmopp(game, room, mrsmopp, tools)
	Mrs_Mopp_Game.createmess(game, room, mess)
	Mrs_Mopp_Game.updategame(game, room, tools, mrsmopp)
	
	# DRAWING
	
	Mrs_Mopp_Game.updatedisplay(mrsmopp, mess, tools, game, room, window)
	
	# END OF CYCLE
	
	clock.tick(game.refreshrate)

pygame.quit
