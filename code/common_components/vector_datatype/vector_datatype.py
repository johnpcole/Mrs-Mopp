import vector_class as VectorClass



def createblank():
	outcome = VectorClass.DefineVector()
	return outcome



def createfromvalues(xval, yval):
	outcome = VectorClass.DefineVector()
	outcome.setfromvalues(xval, yval)
	return outcome



def createfromobject(self, vectorobject):
	outcome = VectorClass.DefineVector()
	outcome.setfromobject(vectorobject)
	return outcome



def sumvectors(first, second):
	outcome = VectorClass.DefineVector()
	outcome.setx(first.getx() + second.getx())
	outcome.sety(first.gety() + second.gety())
	return outcome

