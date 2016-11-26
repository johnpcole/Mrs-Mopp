from ..gui_framework import GUI
from ..vector_datatype import Vector



# -------------------------------------------------------------------
# Get Keyboard Direction changes
# -------------------------------------------------------------------

def getdirectionchange(event):

	outcome = Vector.createfromvalues(0, 0)

	accelerate = getkeychange(event)

	if accelerate != 0:
		if event.key == GUI.K_LEFT:
			outcome.setx(0 - accelerate)
		elif event.key == GUI.K_RIGHT:
			outcome.setx(accelerate)
		elif event.key == GUI.K_UP:
			outcome.sety(0 - accelerate)
		elif event.key == GUI.K_DOWN:
			outcome.sety(accelerate)

	return outcome



# -------------------------------------------------------------------
# Get Keyboard changes
# -------------------------------------------------------------------

def getkeychange(event):

	if event.type == GUI.KEYDOWN:
		outcome = 1
	elif event.type == GUI.KEYUP:
		outcome = -1
	else:
		outcome = 0

	return outcome



# -------------------------------------------------------------------
# Get Special Keyboard Presses
# -------------------------------------------------------------------

def getspecialkeypress(event):

	outcome = "None"

	if getkeychange(event) == 1:
		if event.key == GUI.K_SPACE:
			outcome = "Space"

	return outcome



