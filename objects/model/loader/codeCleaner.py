from lineSorter.lineSorter import LineSorter

class CodeCleaner(object):
	""" cleans invalid commands and formats 
	    the code to be more easy to parse """
	
	def clean(self,codePath):
		ModifiedGCode = ""
		
		with open(codePath, 'r') as input:
			for line in input:
				if((len(line) <= 1) or ("(" in line)):
					continue
				
				line = LineSorter().sort(line.lower())
				
				commands = line.split(' ')
				for command in commands:
					command = command.replace('\n','')
					if(len(command) <= 1):
						continue

					elif (command[0] not in "xyz"):
						ModifiedGCode += command				
						ModifiedGCode += '\n'				

					else:
						ModifiedGCode += command + ' '	
						
					# TODO borrar comandos invalidos
				if(ModifiedGCode[len(ModifiedGCode)-1] != '\n'):
					ModifiedGCode += '\n'		
		return ModifiedGCode