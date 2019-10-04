
from objects.model.parser.parser import Parser
from objects.model.extractor.coordenateValueExtractor import CoordenateValueExtractor

class VelocityChanger(Parser):
	""" used to change the vel for the code """

	def __init__(self,code,levels,cantPoints,newVel):
		""" constructor """
		self.newVel = newVel
		super(self.__class__, self).__init__(code,levels,cantPoints)

	def parse(self,start,end):
		""" inserts points for the (start-end) segment of G-code 
			if the distance between them is lower than the tolerance """
		""" returns the modified G-code and points """
		(self.modifiedGCode,(newStart,newEnd)) = self.changeVel(self.modifiedGCode,start,end)		
		return (super(self.__class__, self).parse(0,0),(newStart,newEnd))


	def changeVel(self,code,start,end):
		""" changes the vel for the code segment """
		lineNum = 0
		oldVel = self.newVel
		g00 = False
		modifiedGCode = ""
		
		(newStart,newEnd) = (start+1,end)
		
		lines = code.split('\n')
		for line in lines:
			if(lineNum < start):
				modifiedGCode += line + "\n"
				if("g00" in line):
					g00 = True
				elif("g01" in line):
					g00 = False
				elif("f" in line):
					oldVel = CoordenateValueExtractor().findCoordValue(line,"f")
				
			elif((lineNum >= start) and (lineNum <= end)):
				if(lineNum == start):
					modifiedGCode += "g01 f" + str(self.newVel) + "\n"
					newEnd+=1
					
				elif(lineNum == end):
					if(g00):
						modifiedGCode += "g00\n"
						newEnd+=1
					modifiedGCode += "f" + str(oldVel) + "\n"			
					newEnd+=1					

				if(line and ("g00" not in line) and ("f" not in line) and ("g01" not in line)):
					modifiedGCode += line + "\n"
				else:
					newEnd-=1
			else:
				if (line):
					modifiedGCode += line + "\n"
			
			lineNum += 1	
		return (modifiedGCode,(newStart,newEnd))
