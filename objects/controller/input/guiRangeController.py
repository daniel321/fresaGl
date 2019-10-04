import wx

class GuiRangeController(object):
	""" handles the user input related to the selection (sliders)"""

	def __init__(self,controller):
		""" constructor """
		self.controller = controller

	def setSliders(self,startSlider,endSlider):
		""" assigns the sliders """
		self.startSlider = startSlider
		self.endSlider = endSlider

	def OnRangeChange(self,event):
		""" asks for a new range and updates it """
		self.controller.askNewRange()	
		
	def OnRangeStartSliderScroll(self,event):
		""" called when the starting slider moves, updates the range and
			prevents it to cross with the ending slider """
		self.correctValues()
		(valMin,valMax) = self.getValues()	
		
		if (valMin and valMax):
			if (valMin >= valMax):
				self.endSlider.SetValue(valMin)

	def OnRangeEndSliderScroll(self,event):
		""" called when the ending slider moves, updates the range and
			prevents it to cross with the starting slider """
		self.correctValues()
		(valMin,valMax) = self.getValues()	
			
		if (valMin and valMax):
			if (valMin >= valMax):
				self.startSlider.SetValue(valMax)
				
	def OnUpdate(self,event):
		""" updates the range and slider values """
		self.correctValues()
		(valMin,valMax) = self.getValues()
		self.controller.setRange(valMin,valMax)

	def updateMaxAndMinValues(self,min,max):
		""" manually assign the max and min values """
		self.startSlider.SetMin(min)
		self.startSlider.SetMax(max)
		
		self.endSlider.SetMin(min)
		self.endSlider.SetMax(max)
		
		self.correctValues()		
		
	def updatePos(self,start,end):	
		""" manually assign the current values """
		self.startSlider.SetValue(float(start))
		self.endSlider.SetValue(float(end))
		self.correctValues()
	
	def getValues(self):
		""" returns the current values """
		valMin = self.startSlider.GetValue()		
		valMax = self.endSlider.GetValue()	
		return (valMin,valMax)
		
	def correctValues(self):
		""" prevents the sliders from crossing or leaving 
			the permitted range """
		valMin = self.startSlider.GetValue()		
		valMax = self.endSlider.GetValue()	
	
		min = self.startSlider.GetMin()
		max = self.startSlider.GetMax()
		
		if (valMin >= max-1):
			valMin = max-1
			self.startSlider.SetValue(max-1)		
		elif (valMin < min):
			valMin = min
			self.endSlider.SetValue(min)
			
		if (valMax <= min+1):
			valMax = min+1
			self.endSlider.SetValue(min+1)	
		
		elif (valMax > max):
			valMax = max
			self.endSlider.SetValue(max)				
	