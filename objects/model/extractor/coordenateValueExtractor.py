
class CoordenateValueExtractor(object):
	""" used to extraxt the value of a coordinate from a G-code line 
	    ej: findCoordValue(self,'g00 x23 y35','x') -> 23 """
	
	def findCoordValue(self,line,coord):
		""" gets the value of the coordinate from a G-code line """		
		posCoord = line.find(coord,0,len(line))
		if (posCoord >= 0):
			posBlk = line.find(" ",posCoord,len(line))
			if(posBlk >= 0):
				val = float(line[posCoord+1:posBlk])
			else:
				val = float(line[posCoord+1:len(line)]) 				
			return val
		return None	
