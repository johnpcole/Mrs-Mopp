from messitem_subcomponent import MessItemClass

class MessLibraryClass:

	def __init__(self):

		#                          Enumeration,       Mess,            Tool, Trigger, Level)
		self.messtype[MessItemClass(          0,    "Dust",       "Dustpan",       7,     1)]
		self.messtype.append(MessItemClass(   1,     "Mug",       "MugTray",       4,     1))
		self.messtype.append(MessItemClass(   2,   "Shirt",   "ShirtBasket",       5,     2))
		self.messtype.append(MessItemClass(   3,   "Glass",     "GlassTray",       6,     3))
		self.messtype.append(MessItemClass(   4,   "Pants",   "PantsBasket",       8,     4))
		self.messtype.append(MessItemClass(-999,    "None",          "None",    -999,  -999))


