from ..common_components.fileprocessing_framework import fileprocessing_module as File
from ..common_components.vector_datatype import vector_module as Vector


# -------------------------------------------------------------------
# Adds images
# -------------------------------------------------------------------

def getimagedata(filenameandpath):

	outcome = []
	rawdata = File.readfromdisk(filenameandpath)

	for dataline in rawdata:
		section = File.extracttabulateddata(dataline)
		sectioncount = len(section)

		if sectioncount == 2:
			iterations = File.extractcommadata(section[1])
			for iteration in iterations:
				outcome.append(section[0] + "\t" + iteration)
		else:
			print "Invalid image data - ", dataline

	return outcome


