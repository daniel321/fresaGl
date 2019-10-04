import os
from objects.utils.files.outputSaver import OutputSaver
from objects.utils.paths import Paths

class M3Launcher(object):
	""" launches mach3 with the modified G-code """
	def __init__(self):
		""" initializes the file saver """
		self.saver = OutputSaver()
	
	def launch(self,code):
		""" saves the current version of the G-code 
			and launches mach3 with it """
		self.saver.saveOutput(code)
		self.saver.saveMacro()

		os.system("runMatch3.bat " + Paths.Instance().mach3Path )
