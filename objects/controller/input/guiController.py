import wx
from objects.utils.files.pathLoader import PathLoader

class GuiController(object):
	""" handles mosts of the buttons in the action window"""

	def __init__(self,controller,frame):
		""" constructor, assigns the controller and frame """
		self.controller = controller
		self.frame = frame
	
	def OnSliderScroll(self,event):
		""" changes the animation speed when the slider moves """
		obj = event.GetEventObject() 
		val = (810-float(obj.GetValue()))/(1000)
		self.controller.changeAnimFreq(val)
		
	def OnTolChange(self,event):
		""" changes the tolerance and adds intermediate points acordingly """
		self.controller.askNewTolerance()
		
	def OnFeedRateChange(self,event):
		""" changes the vel and modifies the G-code acordingly """
		self.controller.askNewVel()
	
	def onChecked(self,event):
		""" toggles weather if all the figure will be shown or only the selection (start,end) """
		state = event.GetEventObject().GetValue()
		self.controller.toggleShowOnlySelection()	
	
	def OnHelp(self,event):
		""" displays the 'help' message """
		self.controller.showHelpMessage()	
		
	def OnEdit(self,event):
		""" launches a text editor to allow the user to modify the selected G-code """
		self.controller.launchTextEditor()
		
	def OnLaunch(self,event):
		""" launches mach3 with the current G-code """
		self.controller.launchMach3()
		
	def OnSelectDraw(self,event):
		""" selects the drawing shape (both,dots,lines) """
		self.controller.setViewShape(event.GetSelection())
		
	def OnSelectAnim(self,event):
		""" selects the drawing mode (all,by level,by points) """
		self.controller.setViewMode(event.GetSelection())	
		
	def OnReset(self,event):
		""" resets the animation """
		self.controller.resetView()		

	def OnSelPrevLvl(self, event):
		""" selects the previous level """
		self.controller.selPrevLvl()	
		
	def OnSelNextLvl(self, event):
		""" selects the next level """
		self.controller.selNextLvl()	
		
	def OnPlay(self, event):
		""" auto advances the animation """
		# self.controller.setViewMode(2)
		self.controller.autoAdvanceView()				
		
	def OnPrev(self, event):
		""" retrocedes the animation once """
		self.controller.retrocedeView()		
	
	def OnNext(self, event):
		""" advances the animation once """
		self.controller.advanceView()		
	
	def OnOpen(self, event):
		""" opens a new G-code file """
		self.controller.loadNewModel()

	def OnExit(self, event):
		""" closes the program """
		self.frame.Show(False)
		self.frame.Close()
		self.controller.close()