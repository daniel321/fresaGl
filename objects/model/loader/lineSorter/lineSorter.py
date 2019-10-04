from comparisonFunction import *

class LineSorter(object):
	""" sorts a line of G-code so we can 
	    analyze it command by command """
	
	def sort(self,line):
		""" sorts a line of code """
		commands = line.split(' ')
		commands.sort(cmp)
		
		line = ""
		for command in commands:
			line += command + " "
		
		return line[:-1]