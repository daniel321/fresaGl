from codeCleaner import CodeCleaner
from objects.model.extractor.pointsExtractor import PointsExtractor

class Loader(object):
	""" used to load the G-code and get the points from it """

	def load(self,codePath,startPoint):
		""" loads the G-code from the .nc file """
		modifiedGCode = CodeCleaner().clean(codePath)
		(levels,cantPoints) = PointsExtractor().extract(modifiedGCode,startPoint)	
		
		return (modifiedGCode,levels,cantPoints)