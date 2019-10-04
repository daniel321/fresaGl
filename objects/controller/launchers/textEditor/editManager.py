import os
from objects.controller.launchers.textEditor.editLauncher import EditLauncher

from objects.utils.files.outputSaver import OutputSaver
from objects.utils.paths import Paths
from objects.utils.files.splitter import Splitter
from objects.utils.files.codeSaver import CodeSaver

from objects.model.loader.codeCleaner import CodeCleaner

class EditManager(object):
	""" edits a part of the G-code and merges it back together """
	def __init__(self,code):
		""" constructor """
		self.code = code
		self.tempPath = Paths.Instance().tempPath		
		
	def editSegment(self,start,end):
		""" lets the user edit the segment (start,end) of the code 
		    and then mershes it together """	
		
		(begCode,midCode,endCode) = Splitter().divideFile(self.code,start,end)

		#print "{" + str(start) + "/" + str(end) + "}"		
		#print "{" + begCode + "}"
		#print "{" + midCode + "}"
		#print "{" + endCode + "}"
				
		EditLauncher().launch(midCode,self.tempPath)
		midCode = CodeCleaner().clean(self.tempPath)
		
		code = begCode + midCode + endCode
		CodeSaver().save(code,self.tempPath)

		newEnd = start + len(midCode.split('\n'))-1
		return (start,newEnd-1)