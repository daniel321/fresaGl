from objects.model.extractor.pointsExtractor import PointsExtractor

class Parser(object):
	""" basic parser, does not modify the code """
	
	def __init__(self,code,levels,cantPoints):
		""" constructor """
		self.modifiedGCode = code
		self.levels = levels
		self.cantPoints = cantPoints
	
	def parse(self,start=0,end=0):	
		""" returns the code and points """
		(self.levels,self.cantPoints) = PointsExtractor().extract(self.modifiedGCode,self.getPoint(start))
		return (self.modifiedGCode,self.levels,self.cantPoints)
	
	def getModifiedGCode(self):
		""" returns the G-code """
		return self.modifiedGCode
		
	def getLevels(self):
		""" returns the points """
		return self.levels
		
	def getCantPoints(self):
		""" returns the amount of points """
		return self.cantPoints
	
	def getPoint(self,n):
		""" returns the point number 'n' of points """
		pos = 0
	
		for level in self.levels:
			for point in level:
				if (pos == n):
					return point
				pos += 1
	
		return [0,0,0,-1]