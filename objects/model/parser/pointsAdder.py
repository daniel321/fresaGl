import math
from objects.model.parser.parser import Parser

class PointsAdder(Parser):
	""" parser used to insert points """
	
	def __init__(self,code,levels,cantPoints,tol):
		""" constructor """
		self.tol = tol
		super(self.__class__, self).__init__(code,levels,cantPoints)
	
	def parse(self,start,end):
		""" inserts points for the (start-end) segment of G-code 
			if the distance between them is lower than the tolerance """
		""" returns the modified G-code and points """
		(self.modifiedGCode,(newStart,newEnd)) = self.addPoints(self.modifiedGCode,self.levels,start,end)		
		return (super(self.__class__, self).parse(0,0),(newStart,newEnd))

	def addPoints(self,code,levels,start,end):
		""" if the distance between points is lower than the tolerance,
			inserts points until that condition is met"""
		
		lastPoint  = levels[0][0]
		tolerance  = self.tol
		
		lines = code.splitlines()
		lineStart = 0
		lineEnd   = len(lines)

		modifiedGCode = ""
		(newStart,newEnd) = (start,end)
		
		for level in levels:
			for point in level:
				if (point[3] > start) and (point[3] <= end):
					dist = self.distance(lastPoint,point)
					
					if(dist > tolerance):
						lineEnd = point[3]

						for lineNum in range(lineStart, lineEnd):
							modifiedGCode += lines[lineNum] + "\n"
						lineStart = lineEnd
						
					while(dist > tolerance):
						nxt = [ lastPoint[0]+(point[0]-lastPoint[0])*(tolerance/dist) , 
								lastPoint[1]+(point[1]-lastPoint[1])*(tolerance/dist) , 
								lastPoint[2]+(point[2]-lastPoint[2])*(tolerance/dist) ]
								
						if(dist < 2*tolerance):
							nxt = [ lastPoint[0]+(point[0]-lastPoint[0])/2 , 
									lastPoint[1]+(point[1]-lastPoint[1])/2 , 
									lastPoint[2]+(point[2]-lastPoint[2])/2 ]
							
						newX = not(nxt[0] == lastPoint[0]);
						newY = not(nxt[1] == lastPoint[1]);
						newZ = not(nxt[2] == lastPoint[2]);

						if (newX):
							modifiedGCode += 'x' + str(nxt[0])							
							if(newY or newZ):
								modifiedGCode += ' '
							else:
								modifiedGCode += '\n'						
						if (newY):
							modifiedGCode += 'y' + str(nxt[1])
							if(newZ):
								modifiedGCode += ' '
							else:
								modifiedGCode += '\n'
						if (newZ):
							modifiedGCode += 'z' + str(nxt[2])						
							modifiedGCode += '\n'

						newEnd+=1							
						lastPoint = [nxt[0],nxt[1],nxt[2],lastPoint[3]]
						dist = self.distance(point,lastPoint)
						
				lastPoint = [point[0],point[1],point[2],point[3]]  
			
		for lineNum in range(lineStart, len(lines)):
			modifiedGCode += lines[lineNum] + "\n"	
			
		return (modifiedGCode,(newStart,newEnd))
		
	def distance(self,point,lastPoint):
		""" returns the distance between the points"""	
	
		diff = [ (point[0]-lastPoint[0]) , (point[1]-lastPoint[1]) , (point[2]-lastPoint[2]) ]
		return math.sqrt( diff[0]*diff[0] + diff[1]*diff[1] + diff[2]*diff[2] )
