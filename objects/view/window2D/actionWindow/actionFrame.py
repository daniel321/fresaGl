
import wx

from objects.view.window2D.elementAdder import ElementAdder

from objects.controller.input.guiController import GuiController
from objects.controller.input.guiRangeController import GuiRangeController

class ActionFrame(wx.Frame):
	""" frame for the action window, creates all the buttons and asigns the callbacks """

	def __init__(self, parent, id, title,iconPath,height,width,style,controller):
		""" initializes all buttons and assigns callbacks """
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,wx.Size(width, height),style=style)
		
		self.adder = ElementAdder(iconPath)	
		self.guiController = GuiController(controller,self)
		self.rangeController = GuiRangeController(controller)
		self.controller = controller
		
		vbox = wx.BoxSizer(wx.VERTICAL)
	
		row1 = self.createFirstRow(self,iconPath)	
		row2 = self.createSecondRow(self,width)						
		
		vbox.Add(row1,0, wx.EXPAND)  
		vbox.Add(row2,0, wx.EXPAND)
		
		self.SetSizer(vbox)
		
	def createFirstRow(self,parent,iconPath):
		""" initializes all buttons and assigns callbacks for the first row """
		toolbar = wx.ToolBar(parent,style=wx.EXPAND)

		self.adder.addButtonWithImage(toolbar,'mach3.png','Launch Mach3',self.guiController.OnLaunch)		
		self.adder.addButtonWithImage(toolbar,'open.png','Open',self.guiController.OnOpen)		
		self.adder.addButtonWithImage(toolbar,'edit.png','Edit',self.guiController.OnEdit)
		self.adder.addButtonWithImage(toolbar,'speed.png','Speed',self.guiController.OnFeedRateChange)
		self.adder.addButtonWithImage(toolbar,'addDots.png','Add Points',self.guiController.OnTolChange)
		self.adder.addButtonWithImage(toolbar,'range.png','Range',self.rangeController.OnRangeChange)	

		for i in range(0, 13):
			toolbar.AddSeparator()			
			
		self.modeCombo = self.adder.addComboBox(toolbar,["All","Layers", "Points"],self.guiController.OnSelectAnim)					
		toolbar.AddSeparator()
		
		self.figureCombo = self.adder.addComboBox(toolbar,["Both","Dots", "Lines"],self.guiController.OnSelectDraw)	
		toolbar.AddSeparator()
		
		self.adder.addButtonWithImage(toolbar,'prev.png','Prev',self.guiController.OnPrev)
		self.adder.addButtonWithImage(toolbar,'antLvl.png','SelectPrevLvl',self.guiController.OnSelPrevLvl)
		self.adder.addButtonWithImage(toolbar,'play.png','Play',self.guiController.OnPlay)		
		self.adder.addButtonWithImage(toolbar,'nextLvl.png','SelectNextLvl',self.guiController.OnSelNextLvl)
		self.adder.addButtonWithImage(toolbar,'next.png','Next',self.guiController.OnNext)
		self.adder.addButtonWithImage(toolbar,'reset.png','Reset',self.guiController.OnReset)		

		toolbar.AddSeparator()
		self.adder.addLabel(toolbar,'Animation\n speed:')
		self.adder.addSlider(toolbar,500,10,800,None,self.guiController.OnSliderScroll)
			
		for i in range(0, 10):
			toolbar.AddSeparator()	

		self.adder.addButtonWithImage(toolbar,'help.png','Help',self.guiController.OnHelp)
		self.adder.addButtonWithImage(toolbar,'exit.png','Exit',self.guiController.OnExit)				
			
		toolbar.Realize()
		return toolbar
	
	def createSecondRow(self,parent,width):
		""" initializes all buttons and assigns callbacks for the second row """
		toolbar = wx.ToolBar(parent,style=wx.EXPAND)	
		
		start = self.adder.addSlider(toolbar,0,0,99999,(int(width*0.45),20),self.rangeController.OnRangeStartSliderScroll,self.rangeController.OnUpdate)		
		self.adder.addButtonWithImage(toolbar,'go.png','UpdateRange',self.rangeController.OnUpdate)
		end = self.adder.addSlider(toolbar,99999,0,99999,(int(width*0.45),20),self.rangeController.OnRangeEndSliderScroll,self.rangeController.OnUpdate)

		self.rangeController.setSliders(start,end)
		
		self.adder.addCheckbox(toolbar,'Show All',self.guiController.onChecked)
		
		toolbar.Realize()	
		return toolbar	
	
	def updateSliderRange(self,max,min):
		""" updates the range for the sliders on the second row"""
		if(self.rangeController):
			self.rangeController.updateMaxAndMinValues(max,min)
	
	def updateSliderPos(self,start,end):
		""" updates the position for the sliders on the second row"""
		self.rangeController.updatePos(start,end)	
	
