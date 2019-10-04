import wx

class InputAsker(object):
	""" class used to display popups asking for values """
	
	def askNewTolerance(self,defaultValue):
		""" asks the user for the new value for the tolerance """
		tolMsg = "Insert tolerance in mm (min distance to insert points):"

		dlg = wx.TextEntryDialog(None, tolMsg, defaultValue=str(defaultValue))
		dlg.ShowModal()

		value = float(dlg.GetValue())
		dlg.Destroy()
		
		if(value and (value != str(defaultValue)) ):
			return value
		return None
		
	def askNewVel(self,defaultValue):
		""" asks the user for the new value for the feed rate """
		feedRateMsg = "Insert feedRate (machine speed): "

		dlg = wx.TextEntryDialog(None, feedRateMsg, defaultValue=str(defaultValue))
		dlg.ShowModal()
		
		value = dlg.GetValue()
		dlg.Destroy()
		
		if(value != str(defaultValue)):
			return float(value)
		return None
		
	def askNewRange(self,default):
		""" asks the user for the new (start;end) that define the selected range """	
		rangeMsg = "Insert the working range:"
		defaultValue = str(default[0])
		defaultValue += ";"
		defaultValue += str(default[1])
		
		dlg = wx.TextEntryDialog(None, rangeMsg, defaultValue=str(defaultValue))
		dlg.ShowModal()

		value = dlg.GetValue()

		dlg.Destroy()
		if(value != defaultValue):
			range = dlg.GetValue().split(";")
			start = float(range[0])
			end = float(range[1]) 
			return (start,end)
		return (None,None)
