from objects.controller.launchers.m3Launcher import M3Launcher 
from objects.controller.launchers.textEditor.editManager import EditManager


class LauncherController(object):
	""" controller used for launching other applications """
	
	def __init__(self,view,codeWindow,actionWindow):	
		""" constructor """
		self.view = view
		self.codeWindow = codeWindow
		self.actionWindow =	actionWindow	
		
	def launchMach3(self,code):
		""" launches mach3 with the current G-code """
		self.view.hide()
		self.codeWindow.hide()
		self.actionWindow.hide()
			
		M3Launcher().launch(code)

		self.view.show()
		self.codeWindow.show()
		self.actionWindow.show()

	def launchTextEditor(self,code,start,end):
		""" launches a text editor with the current selection of the G-code """
		self.view.hide()
		self.codeWindow.hide()
		self.actionWindow.hide()
			
		(start,end) = EditManager(code).editSegment(start,end)

		self.view.show()
		self.codeWindow.show()
		self.actionWindow.show()
			
		return (start,end)