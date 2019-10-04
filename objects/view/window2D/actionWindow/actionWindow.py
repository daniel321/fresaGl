
import wx
from objects.utils.paths import Paths


from actionFrame import ActionFrame 


class ActionWindow(wx.App):
	""" window with all the buttons and stuff for the user to interact with the system"""

	def __init__(self,width,height,pos):
		""" constructor """
		super(self.__class__, self).__init__()
		self.height = height
		self.width = width
		self.pos = pos

	def initialize(self,controller):
		""" creates the frame with all the buttons and other stuff"""
		self.controller = controller
		
		iconPath = Paths.Instance().iconPath	

		#wx.STAY_ON_TOP 
		style = ( wx.NO_BORDER | wx.STAY_ON_TOP)
		self.frame = ActionFrame(None, -1, '',iconPath,self.height,self.width,style,self.controller)
		self.frame.SetPosition(self.pos)
		self.show()
		self.frame.SetFocus()
	
		return True
		
	def updateSliderRange(self,max,min):
		""" changes the range for the selection sliders"""
		self.frame.updateSliderRange(max,min)
		
	def updateSliderPos(self,start,end):
		""" changes the position for the selection sliders"""
		self.frame.updateSliderPos(start,end)
		
	def hide(self):
		""" hides the action window """
		self.frame.Show(False)
		
	def show(self):
		""" shows the action window """
		self.frame.Show(True)