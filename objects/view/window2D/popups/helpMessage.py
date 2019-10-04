import wx

class HelpMessage(object):
	""" class used to display the 'help' message """
	
	def showHelpMessage(self):
		""" displays the 'help' message """


		self.helpMsg = "Camera movments:"
		self.helpMsg += "Up = q\n"
		self.helpMsg += "Down = e\n"
		self.helpMsg += "Left = a\n"
		self.helpMsg += "Right = d\n"
		self.helpMsg += "Forward = w\n"
		self.helpMsg += "Backwards = s\n"
		self.helpMsg += "\n"
		self.helpMsg += "Rotate left = Left arrow\n"
		self.helpMsg += "Rotate right = Right arrow\n"
		self.helpMsg += "Rotate up = Up arrow\n"
		self.helpMsg += "Rotate down = Down arrow\n"
		self.helpMsg += "\n"		
		self.helpMsg += "Program functions:\n"
		self.helpMsg += "Load model = Spacebar\n"
		self.helpMsg += "Manual edit = Intro\n"
		self.helpMsg += "Launch Mach3 = Enter\n"
		self.helpMsg += "Change vel = numpad_1\n"
		self.helpMsg += "Change tolerance = numpad_2\n"
		self.helpMsg += "Change selection range = numpad_3\n"
		self.helpMsg += "Quit = Esc\n"
		self.helpMsg += "\n"
		self.helpMsg += "Animation:\n"
		self.helpMsg += "Reset = numpad_0\n"
		self.helpMsg += "Play = numpad_5\n"
		self.helpMsg += "Prev animation frame= numpad_4\n"
		self.helpMsg += "Next animation frame= numpad_6\n"
		self.helpMsg += "Select prev level = numpad_7\n"
		self.helpMsg += "Select next level = numpad_9\n"
		
		box    = wx.MessageDialog(None,self.helpMsg,"Help",wx.OK)
		answer = box.ShowModal()
		box.Destroy()