import os

class CodeSaver(object):
	""" saves the modified G-code to the requested path """

	def save(self,code,path):
		""" saves the code to the requested path """
		outputFile = open(path, 'w')
		outputFile.write(code)
		outputFile.close()