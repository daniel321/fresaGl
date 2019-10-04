import math
import random

from OpenGL.GL import *
from OpenGL.GLU import *

from objects.utils.vector3 import Vector3

class FigureView(object):
	""" represents the 3d image with all the movments the machine will produce """
	
	def __init__(self,scale):
		""" initializes an empty figure"""
		self.levels = []

		self.scale = scale

		self.actualPoint = 0
		self.actualLvl = 0

		self.shapes = ["Both","Dots", "Lines"]
		self.cantShapes = 3
		self.shape = 0

		self.modes = ["All","Layers", "Points"]
		self.cantModes = 3
		self.mode = 0

		self.cantPoints = 0		
		
		(self.start,self.end) = (0,999999)
		self.showSelection = True

		self.pointSize     = 3
		self.lineSize 	   = 1
		
	def toggleShowOnlySelection(self,start):
		""" toggles weather to show all figure or only the selected area """
		self.showSelection = not self.showSelection
		self.resetView(start)
		
		return self.showSelection
	
	def resetView(self,start):
		""" clears and rewinds the animation """
		self.actualLvl = 0
		
		if(self.showSelection):
			self.actualPoint = self.getSelectionStartPoint(start)
		else:
			self.actualPoint = 0
	
	def getSelectionStartPoint(self,start):
		""" returns the firt point of the selected area """
		numpoint = 0
			
		for level in self.levels:
			for point in level:
				if(point[3] == start):
					return numpoint
				numpoint +=1
		return 0
	
	def setLevels(self,levels,cantPoints,start,end):
		""" assigns the list of points and range """
		self.levels = levels
		self.cantPoints = cantPoints
		self.actualLvl = 0
		self.shape = 0
		self.mode = 0
		(self.start,self.end) = (start,end)

	def increaseLvl(self):
		""" increases the level to show in the mode that shows only the current level """
		cantLvls = len(self.levels)
		if(cantLvls > 0):	
			self.actualLvl = (self.actualLvl+1)%(cantLvls)

	def decreaseLvl(self):
		""" decreases the level to show in the mode that shows only the current level """
		if(self.actualLvl > 0):
			self.actualLvl = self.actualLvl-1

	def increasePoint(self):
		""" increases the 'actualPoint' to show in the mode that shows only until the 'actualPoint' """
		cantPoints = self.cantPoints
		if(cantPoints and cantPoints > 0):
			self.actualPoint = (self.actualPoint+1)%(cantPoints+1)

	def decreasePoint(self):
		""" decreases the 'actualPoint' to show in the mode that shows only until the 'actualPoint' """
		if(self.actualPoint > 0):
			self.actualPoint = self.actualPoint-1	
			
	def changeViewMode(self):
		""" changes the current view mode (all,byLevels,byPoints) """
		self.mode = (self.mode + 1)%self.cantModes 

	def setViewMode(self,mode):
		""" changes the current view mode (all,byLevels,byPoints) """
		self.mode = (mode)%self.cantModes 		
		
	def changeViewShape(self):
		""" changes the current view shape (both,points,lines) """
		self.shape = (self.shape + 1)%self.cantShapes 	

	def setViewShape(self,shape):
		""" changes the current view shape (both,points,lines) """
		self.shape = (shape)%self.cantShapes 
			
	def render(self):
		""" renders the image acording to the current configuration """
		
		if ( (self.shapes[self.shape] == "Both") and (self.modes[self.mode] == "All") ):	
			self.drawAllPoints()
			self.drawAllLines()	
			self.drawFirstAndLastPoint()
				
		elif ( (self.shapes[self.shape] == "Dots") and (self.modes[self.mode] == "All") ):			
			self.drawAllPoints()
			self.drawFirstAndLastPoint()
			
		elif ( (self.shapes[self.shape] == "Lines") and (self.modes[self.mode] == "All") ):			
			self.drawAllLines()	
			self.drawFirstAndLastPoint()			

		elif ( (self.shapes[self.shape] == "Both") and (self.modes[self.mode] == "Layers") ):			
			self.drawActualLvlPoints()
			self.drawActualLvlLines()
			self.drawFirstAndLastPointOfTheLvl()
			
		elif ( (self.shapes[self.shape] == "Dots") and (self.modes[self.mode] == "Layers") ):			
			self.drawActualLvlPoints()
			self.drawFirstAndLastPointOfTheLvl()

		elif ( (self.shapes[self.shape] == "Lines") and (self.modes[self.mode] == "Layers") ):			
			self.drawActualLvlLines()
			self.drawFirstAndLastPointOfTheLvl()

		elif ( (self.shapes[self.shape] == "Both") and (self.modes[self.mode] == "Points") ):
			self.drawUntilPointPoints()	
			self.drawUntilPointLines()	
			
		elif ( (self.shapes[self.shape] == "Dots") and (self.modes[self.mode] == "Points") ):	
			self.drawUntilPointPoints()
			
		elif ( (self.shapes[self.shape] == "Lines") and (self.modes[self.mode] == "Points") ):		
			self.drawUntilPointLines()
	
	def scalePoint(self,point):
		""" scales the point """
		return (point[0]/self.scale,point[1]/self.scale,point[2]/self.scale)
	
	def drawFirstAndLastPointOfTheLvl(self):
		""" draws the first (green) and last point(red) of the level as a reference """	
		if ((len(self.levels) >= 1) and (len(self.levels[self.actualLvl]) > 1)):
			glColor([0,1,0])
			glPointSize(2*self.pointSize)
			glBegin(GL_POINTS)
			point = self.levels[self.actualLvl][0]
			glVertex( self.scalePoint(point) )			
			glColor([1,0,0])
			point = self.levels[self.actualLvl][len(self.levels[self.actualLvl])-1]
			glVertex( self.scalePoint(point) )	
			glEnd()

	def drawFirstAndLastPoint(self):
		""" draws the first (green) and last point(red) of the figure as a reference """		
		if (len(self.levels) >= 1):
			glColor([0,1,0])
			glPointSize(2*self.pointSize)
			glBegin(GL_POINTS)
			point = self.levels[0][0]
			glVertex( self.scalePoint(point) )			
			glColor([1,0,0]) 
			point = self.levels[-1][-1]
			glVertex( self.scalePoint(point) )	
			glEnd()
			
	def drawUntilPoint(self):
		""" draws all points until the 'actualPoint' """
		""" if showSelection is on, only shows selected points """		
		pos = 0
		lvl = 0
		
		while((pos <= self.actualPoint) and (len(self.levels) > lvl)):
			color = [0,0,1]
			for point in self.levels[lvl]:
				
				if(pos >= self.actualPoint):
					return
			
				if((point[3] > self.start) and (point[3] <= self.end )):
					glColor([1,0,0])
				else:
					glColor(color)	
					
				if(self.start == 0 and self.start == pos):
					glVertex( self.scalePoint(point) )
					
				notSelection = (not self.showSelection)
				inRange = ((point[3] >= self.start) and (point[3] <= self.end ))
				
				if( notSelection or inRange):
					glVertex( self.scalePoint(point) )
				
				pos = pos+1
			lvl = lvl+1
	
	def drawUntilPointPoints(self):
		""" draws all points until the 'actualPoint' using only points """
		""" if showSelection is on, only shows selected points """	
		glPointSize(self.pointSize)
		glBegin(GL_POINTS)
		self.drawUntilPoint()	
		glEnd()	

	def drawUntilPointLines(self):
		""" draws all points until the 'actualPoint' using only lines """
		""" if showSelection is on, only shows selected points """	
		glLineWidth(self.lineSize)
		glBegin(GL_LINE_STRIP)
		self.drawUntilPoint()
		glEnd()
		
	def drawActualLvl(self):
		""" draws the current level of the figure """
	
		glColor([0,0,1])
		if(len(self.levels) > self.actualLvl):
			for point in self.levels[self.actualLvl]:
				glVertex( self.scalePoint(point) )

	def drawActualLvlPoints(self):
		""" draws the current level of the figure using only points"""
		glPointSize(self.pointSize)
		glBegin(GL_POINTS)
		self.drawActualLvl()
		glEnd()
	
	def drawActualLvlLines(self):
		""" draws the current level of the figure using only lines"""
		glLineWidth(self.lineSize)
		glBegin(GL_LINE_STRIP)
		self.drawActualLvl()
		glEnd()	
			
	def drawAll(self):
		""" draws all the figure"""
		""" if showSelection is on, only shows selected points """
		pos = 0
		for level in self.levels:
			color = [0,0,1]
			for point in level:	
				if((point[3] > self.start) and (point[3] <= self.end)):
					glColor([1,0,0])
				else:
					glColor(color)	
					
				notSelection = (not self.showSelection)
				first = (self.start == 0) and (point[3] == -1)
				inRange = ((point[3] >= self.start) and (point[3] <= self.end))

				if( first or notSelection or inRange):
					glVertex( self.scalePoint(point) )
				
				pos += 1
	
	def drawAllPoints(self):
		""" draws all the figure using only points """
		""" if showSelection is on, only shows selected points """
		glPointSize(self.pointSize)
		glBegin(GL_POINTS)
		self.drawAll()
		glEnd()	
	
	def drawAllLines(self):
		""" draws all the figure using only lines """
		""" if showSelection is on, only shows selected points """
		glLineWidth(self.lineSize)
		glBegin(GL_LINE_STRIP)
		self.drawAll()
		glEnd()	
		
	def getRandomColor(self,pastel_factor=0.5):
		""" returns a random color (r,g,b) """
		x = (float(random.uniform(0,1.0))+float(pastel_factor))/(1.0+float(pastel_factor));
		y = (float(random.uniform(0,1.0))+float(pastel_factor))/(1.0+float(pastel_factor));
		z = (float(random.uniform(0,1.0))+float(pastel_factor))/(1.0+float(pastel_factor));
	
		return [x,y,z]	
