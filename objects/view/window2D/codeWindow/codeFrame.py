import wx

class CodeFrame(wx.Frame):
	""" controller for the window that displays the current G-code """
	
	def __init__(self, parent, id, title,height,width,style,codeStyle):	
		""" initializes the frame """
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(width, height),style = style)
		
		self.width = width 
		self.height = height
		
		self.code = wx.TextCtrl(self,size=(self.width, self.height), style = codeStyle) 
		self.Show()
		
		
	def loadCode(self,code,startNum):
		""" loads new code to display """
		self.code.Clear()
		lines = code.split('\n')
		fileBuffer = ""

		numLine = startNum
		for x in range(0, len(lines)):
			line = lines[x]
			if (x<len(lines)-1):
				fileBuffer += str(numLine) + ".\t " + line + "\n"
			numLine += 1

		self.code.AppendText(fileBuffer)
