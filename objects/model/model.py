import math
import random
import os

import OpenGL.GL
import OpenGL.GLU

from objects.utils.matrix44 import Matrix44


from parser.parser import Parser
from parser.velocityChanger import VelocityChanger
from parser.pointsAdder import PointsAdder
from loader.loader import Loader 

class Model(object):
	""" contains the edited G-code and the point seq """
	
	def __init__(self,path):
		""" constructor """
		self.changePath(path)
	
	def generateModel(self,startPoint,start,end,tol,vel):
		""" applies the required parsers to the G-code """
		
		(code,levels,cantPoints) = Loader().load(self.path,startPoint)
		haveParser = False

		added = 0
		self.start = start
		self.end   = end
		
		if( tol > 0):		
			self.parser = PointsAdder(code,levels,cantPoints,tol)
			((code,levels,cantPoints),(self.start,self.end)) = self.parser.parse(self.start,self.end)
			haveParser = True
			
		if( vel > 0):		
			self.parser = VelocityChanger(code,levels,cantPoints,vel)
			((code,levels,cantPoints),(self.start,self.end)) = self.parser.parse(self.start,self.end)
			haveParser = True
			
		if (not haveParser):
			self.parser = Parser(code,levels,cantPoints)
			(code,levels,cantPoints) = self.parser.parse()	
	
		self.modifiedGCode = code
		self.levels = levels
		self.cantPoints = cantPoints

	def getNextLvl(self,start):
		""" returns the range (start,end) for the next level 
			starting from 'start' """	
		levels = self.parser.getLevels()

		for level in levels:
			first = level[0]
			if(first and first[3] > start):
				last = level[-1]
				return (first[3],last[3])

		if(not first):
			return (0,999999)
		else:
			return(levels[-1][0][3],levels[-1][-1][3])

	def getPrevLvl(self,start):
		""" returns the range (start,end) for the previous level 
			starting from 'start' """	
		levels = self.parser.getLevels()
		
		prev = -1
		for level in levels:
			if(prev == -1):
				prev = level
			else:
				if(level[0] and level[0][3] >= start):
					return (prev[0][3],prev[-1][3])
				prev = level

		return (0,999999)
		
	def changePath(self,path):
		""" sets the new filePath for the G-code """
		self.path = path
	
	def getModifiedGCode(self):
		""" returns the G-code """
		return self.parser.getModifiedGCode()
	
	def getLevels(self):
		""" returns the points """
		return self.parser.getLevels()
		
	def getCantPoints(self):
		""" returns the amount of points """
		return self.parser.getCantPoints()
	
	def getCantLines(self):
		""" returns the amount of lines in the G-code """	
		return len(self.getModifiedGCode().split('\n'))
	
	def getFinalRange(self):
		""" returns the range after making the modification to the G-code """	
		return (self.start,self.end)
