import os
from objects.utils.files.outputSaver import OutputSaver
from objects.utils.files.codeSaver import CodeSaver

from objects.utils.paths import Paths

class EditLauncher(object):
	""" lets the user edit a segment of G-code using a text editor """
		
	def launch(self,code,path):
		""" launches the text editor with the modified G-code """
		CodeSaver().save(code,path)
		editor = Paths.Instance().textEditorPath
		os.system('"'+editor +'" ' + str(path.split("/")[-1]))
