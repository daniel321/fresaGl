from math import pi

from OpenGL.GL import *
from OpenGL.GLU import *

from objects.utils.vector3 import Vector3

import math

class Axis(object):
	""" axis 3d """
	
	def __init__(self,scale):
		""" constructor """
		self.scale = scale

	def render(self):
		""" renders a visual representation of the x-y-z axis 
			scaled acordingly """

		posArr = 3500
		length = 3200

		glColor( (0.5, 0.0, 0.0) )
		glBegin(GL_LINES)	
		self.renderXaxis(length)
		glEnd()

		glBegin(GL_TRIANGLE_STRIP)
		self.renderConeX([posArr,0,0],0.5,5)
		glEnd()

		glColor( (0.0, 0.5, 0.0) )
		glBegin(GL_LINES)	
		self.renderYaxis(length)
		glEnd()

		glBegin(GL_TRIANGLE_STRIP)
		self.renderConeY([0,posArr,0],0.5,5)
		glEnd()

		glColor( (0.0, 0.0, 0.5) )	
		glBegin(GL_LINES)	
		self.renderZaxis(length)
		glEnd()

		glBegin(GL_TRIANGLE_STRIP)
		self.renderConeZ([0,0,posArr],0.5,5)
		glEnd()

	def renderXaxis(self,length):
		""" renders the x-axis"""	
		glVertex( (-length/self.scale, 0,  0) )		
		glVertex( (   0, 0,	 0) )			 
		glVertex( (   0, 0,  0) )
		glVertex( ( length/self.scale, 0,  0) ) 

#		descomentar para ver marcas cada 1cm (realentiza animacion)
		for i in range(-length, length):
			glVertex( (	i/self.scale, -5.0/self.scale,               0) )
			glVertex( (	i/self.scale,  5.0/self.scale,               0) )
#			glVertex( (	i/self.scale,               0, -5.0/self.scale) )
#			glVertex( (	i/self.scale,               0,  5.0/self.scale) )

	def renderYaxis(self,length):
		""" renders the y-axis"""	
		glVertex( (	 0,-length/self.scale, 0) ) 
		glVertex( (	 0,   0, 0) ) 
		glVertex( (	 0,   0, 0) ) 		
		glVertex( (	 0, length/self.scale, 0) ) 

#		descomentar para ver marcas cada 1cm (realentiza animacion)
		for i in range(-length, length):
			glVertex( (	-5.0/self.scale,i/self.scale,               0) )
			glVertex( (	 5.0/self.scale,i/self.scale,               0) )
#			glVertex( (	              0,i/self.scale, -5.0/self.scale) )
#			glVertex( (	              0,i/self.scale,  5.0/self.scale) )

	def renderZaxis(self,length):
		""" renders the z-axis"""	
		glVertex( (	 0,	 0,-length/self.scale) ) 
		glVertex( (	 0,  0,   0) ) 		
		glVertex( (	 0,  0,	  0) ) 			
		glVertex( (	 0,	 0, length/self.scale) ) 	

#		descomentar para ver marcas cada 1cm (realentiza animacion)
		for i in range(-length, length):
			glVertex( (	              0, -5.0/self.scale, i/self.scale) )
			glVertex( (	              0,  5.0/self.scale, i/self.scale) )
#			glVertex( (	-5.0/self.scale,               0, i/self.scale) )
#			glVertex( (	 5.0/self.scale,               0, i/self.scale) )

	def renderConeX(self,center,r,dist):
		""" 3d cone indicating the positive direction of the x-axis """
		res = 25
		for i in range(0, res+1):
			x = float(2*pi/res)*i;
			glVertex( ( center[0]/self.scale, center[1]/self.scale, center[2]/self.scale) )	
			glVertex( ( center[0]/self.scale-dist, r*math.cos(x), r*math.sin(x)) )					
	
	def renderConeY(self,center,r,dist):
		""" 3d cone indicating the positive direction of the y-axis """	
		res = 25
		for i in range(0, res+1):
			x = float(2*pi/res)*i;
			glVertex( ( center[0]/self.scale, center[1]/self.scale, center[2]) )	
			glVertex( ( r*math.cos(x), center[1]/self.scale-dist, r*math.sin(x)) )					

	def renderConeZ(self,center,r,dist):
		""" 3d cone indicating the positive direction of the z-axis """	
		res = 25
		for i in range(0, res+1):
			x = float(2*pi/res)*i;
			glVertex( ( center[0]/self.scale, center[1]/self.scale, center[2]/self.scale) )	
			glVertex( ( r*math.sin(x), r*math.cos(x), center[2]/self.scale-dist) )						