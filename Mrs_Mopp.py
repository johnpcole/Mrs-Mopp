from codebase import MrsMopp



print "Application Started"
MrsMopp.runprogram()
print "Application Ended"

#
#
#
# import pygame
# import code.definitions_component
# import code.common_components
#
# pygame.init()
# clock = pygame.time.Clock()
# window = Mrs_Mopp_Definitions.preparewindow()
#
# from code.player_component import PlayerClass
# from code.room_component import RoomClass
# from code.mess_component import MessClass
# from code.tools_component import ToolClass
# from code.game_component import GameClass
#
# room = RoomClass()
# mrsmopp = PlayerClass()
# mess = MessClass()
# tools = ToolClass()
# game = GameClass()
#
# Mrs_Mopp_Game.preparegame(game, room, tools, window)
#
# quitscreen = False
# while quitscreen == False:
#
# 	# EVENT PROCESSING
#
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			quitscreen = True
# 		else:
# 			Mrs_Mopp_Game.operategame(mrsmopp, tools, event)
#
# 	# GAME LOGIC
#
# 	Mrs_Mopp_Game.movemrsmopp(game, room, mrsmopp, tools)
# 	Mrs_Mopp_Game.createmess(game, room, mess)
# 	Mrs_Mopp_Game.updategame(game, room, tools, mrsmopp)
#
# 	# DRAWING
#
# 	Mrs_Mopp_Game.updatedisplay(mrsmopp, mess, tools, game, window)
#
# 	# END OF CYCLE
#
# 	clock.tick(game.refreshrate)
#
# pygame.quit
