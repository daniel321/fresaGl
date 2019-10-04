import wx

class ElementAdder(object):
	""" class used to initialize different widgets on the windows """
	def __init__(self,iconPath):
		""" constructor """
		self.num = 0
		self.iconPath = iconPath
		
	def addButtonWithImage(self,toolbar,path,text,method):
		""" adds an image that works like a button and binds the 'click' action to the method """
		self.num += 1
		toolbar.AddSimpleTool(self.num,wx.Image(self.iconPath+path, wx.BITMAP_TYPE_PNG).ConvertToBitmap(),text, '')
		toolbar.Bind(wx.EVT_TOOL, method, id=self.num)
	
	def addComboBox(self,toolbar,choices,method):
		""" adds a combo box and binds the 'OnChanged' action to the method """
		combo = wx.ComboBox(toolbar, -1,choices=choices,style=wx.CB_READONLY)		
		toolbar.AddControl(combo) 
		combo.Bind(wx.EVT_COMBOBOX,method)		
		return combo
		
	def addCheckbox(self,toolbar,label,method):
		""" adds a check box and binds the 'OnToggled' action to the method """
		checkbox = wx.CheckBox(toolbar,label = label) 
		toolbar.AddControl(checkbox)
		checkbox.Bind(wx.EVT_CHECKBOX,method)
		return checkbox

	def addSlider(self,toolbar,start,min,max,size,method,method2=None):
		""" adds a slider and binds the 'OnChanged' action to the method """	
		slider = wx.Slider(toolbar,value = start, minValue = min, maxValue = max,style = wx.SL_HORIZONTAL)
		toolbar.AddControl(slider)
		slider.Bind(wx.EVT_SLIDER, method)

		if(method2):
			slider.Bind(wx.EVT_SCROLL_THUMBRELEASE,method2)

		return slider
		
	def addLabel(self,toolbar,label):
		""" adds a label """
		label = wx.StaticText(toolbar, label = label,style = wx.ALIGN_CENTER)  		
		toolbar.AddSeparator()
		toolbar.AddControl(label)	
		
		return label
