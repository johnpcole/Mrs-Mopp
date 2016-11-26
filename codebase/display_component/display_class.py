from ..Common_Components import AppDisplay



class DefineDisplay:
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================



	def __init__(self, field):

		# Sets up pygame window related properties & methods and loads images
		self.appwindow = AppDisplay.createappwindow(field.getsize(), "Mrs Mopp")



	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================

	def paintimage(self, icon, position):
		self.appwindow.drawimage(icon, position.getscaled(20))





	# -------------------------------------------------------------------
	# Updates all elements of the screen, flips the display, then
	# removes embellishments from the field ready for the next cycle
	# -------------------------------------------------------------------





	# ==========================================================================================
	# Get Information
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Returns the plaque animation frame, either 1 or 2 AS A STRING
	# -------------------------------------------------------------------



