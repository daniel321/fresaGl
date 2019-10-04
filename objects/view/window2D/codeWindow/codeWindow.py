
import wx
from objects.utils.files.splitter import Splitter
from codeFrame import CodeFrame 

class CodeWindow(wx.App):
	""" window used to display the current G-code """

	def __init__(self,width,height,pos):
		""" constructor """
		super(self.__class__, self).__init__()
		self.height = height
		self.width = width
		self.pos = pos

	def initialize(self):
		""" initializes the code window """

		#wx.STAY_ON_TOP 
		style = ( wx.NO_BORDER | wx.STAY_ON_TOP)
		codeStyle = (wx.TE_MULTILINE | wx.TE_READONLY )
		self.frame = CodeFrame(None, -1, '',self.height,self.width,style,codeStyle)
		self.frame.SetPosition(self.pos)
		self.show()
	
		self.showOnlySelection = True
		return True
		
	def update(self,newCode,start,end):
		""" updates the code displayed in the window to reflect the selection """
		""" if 'showOnlySelection' is false displays all the code """
		startLine = 0

		if(self.showOnlySelection):
			startLine = start
			(begCode,newCode,endCode) = Splitter().divideFile(newCode,start,end)		
			
		self.loadCode(newCode,startLine)	
	
	def toggleShowOnlySelection(self):
		""" toggles weather if show all the code or only the selected segment """
		self.showOnlySelection = not self.showOnlySelection
	
	def loadCode(self,code,startNum):
		""" changes the code to be shown within the window """
		self.frame.loadCode(code,startNum)
		
	def hide(self):
		""" hides the code window """
		self.frame.Show(False)
		
	def show(self):
		""" shows the code window """
		self.frame.Show(True)