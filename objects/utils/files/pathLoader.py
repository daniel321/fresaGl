from Tkinter import Tk
import tkFileDialog

class PathLoader(object):
	""" gets the file path for the G-code to display """
	
	def loadPath(self):
		""" asks for the filepath and returns it """
		Tk().withdraw()
		path = tkFileDialog.askopenfilename()
		if (not path):
			return None
		
		return path
