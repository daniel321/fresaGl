from coordenateValueExtractor import CoordenateValueExtractor

class PointsExtractor(object):
	""" used to get all the points from the G-code 
	    with the purpose of rendering them later """
		
	def extract(self,code,startPoint):
		""" extracts the points from the G-code """
		levels = []
		level = []
		
		level.append([startPoint[0],startPoint[1],startPoint[2],startPoint[3]])
		
		point = startPoint
		lastPoint = startPoint
		cantPoints = 1
		lineNum = 0
		
		for line in code.splitlines():	
			while( (len(line) > 0) and (line[0] == ' ') ):
				line = line[1:]
				
			if(len(line) <= 0):
				continue

			elif(line[0] in "xyz"):	
				x = CoordenateValueExtractor().findCoordValue(line,"x")
				if(not (x is None)):				
					point[0] = x
					
				y = CoordenateValueExtractor().findCoordValue(line,"y")
				if(not (y is None)):				
					point[1] = y

				z = CoordenateValueExtractor().findCoordValue(line,"z")
				if(not (z is None)):				
					point[2] = z
					
					if (point[2] < lastPoint[2]):
						levels.append(level)
						level = []

				point[3] = lineNum						
				if((point[0],point[1],point[2],point[3]) != (lastPoint[0],lastPoint[1],lastPoint[2],lastPoint[3])):
					level.append(point)
					
					cantPoints += 1
				point = [point[0],point[1],point[2],lineNum]
				lastPoint = [point[0],point[1],point[2],lineNum]
				
			lineNum += 1

		levels.append(level)
		
		return (levels,cantPoints)