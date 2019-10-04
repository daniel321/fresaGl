import os
from objects.utils.paths import Paths

from codeSaver import CodeSaver

class OutputSaver(object):
	""" used to the program output """
		
	def __init__(self):
		""" constructor """
		self.savePath = Paths.Instance().savePath
		self.macroPath = Paths.Instance().macroPath
	
	def saveOutput(self,code):
		""" saves the code in the corresponding path """
		CodeSaver().save(code,self.savePath)

	def saveMacro(self):
		""" creates a macro for mach3 so it automatically loads the G-code on startup """
		CodeSaver().save('Loadfile("'+ self.savePath + '")',self.macroPath)