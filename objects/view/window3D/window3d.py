import math,os
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from objects.view.window3D.models3D.figureView import FigureView
from objects.view.window3D.models3D.axis import Axis

import logging
logging.basicConfig()

class Window3d(object):
	""" window used to draw the 3d figure """
	
	def __init__(self,width,height,pos):
		""" constructor """
		scale = 100
		self.figureView = FigureView(scale)
		self.axis = Axis(scale)
		self.display_list = None
		self.autoadvance = False
		self.autoretrocede = False
		self.acumTime = 0
		self.animTime = 1.0
		
		self.height = height
		self.width = width
		self.pos = pos

	def initView(self):
		""" initializes the window and OpenGl """	
		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % self.pos
		screen = pygame.display.set_mode((self.width, self.height), HWSURFACE|OPENGL|DOUBLEBUF)
		self.resize(self.width, self.height)
		
		glEnable(GL_DEPTH_TEST)
	
		glShadeModel(GL_FLAT)
		glClearColor(1.0, 1.0, 1.0, 0.0)

		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_VERTEX_PROGRAM_POINT_SIZE)
	
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)		
		glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0))	
	
		glMaterial(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))	
		glMaterial(GL_FRONT, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
	
	def resize(self,width, height):
		""" resizes the window """
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(60.0, float(width)/height, .1, 1000.)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def hide(self):
		""" hides the window """
		pygame.display.quit()
		
	def show(self):
		""" shows the window """
		self.initView()
		self.setRedraw()
		
	def clearScreen(self):
		""" clears the OpenGL rendering """
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	def setRedraw(self):	
		""" sets it so the figure will be redrawn in the next cycle """
		self.display_list = None

	def toggleShowOnlySelection(self,start):
		""" toggles weather to show all the figure or only the selected area """
		return self.figureView.toggleShowOnlySelection(start)
		
	def changeViewMode(self):
		""" swaps between drawing (all, by layer, by points) """
		self.figureView.changeViewMode()
		self.setRedraw()

	def setViewMode(self,mode):
		""" selects the drawing mode: (all, by layer, by points) """
		self.figureView.setViewMode(mode)
		self.setRedraw()
		
	def changeViewShape(self):
		""" swaps between drawing shapes: (both,dots,lines) """
		self.figureView.changeViewShape()
		self.setRedraw()

	def setViewShape(self,shape):
		""" selects the drawing shape: (both,dots,lines) """
		self.figureView.setViewShape(shape)
		self.setRedraw()

	def resetView(self,start):
		""" clears and resets the animation """
		self.figureView.resetView(start)
		self.setRedraw()
		
	def increase(self):
		""" advances the animation one step """
		self.figureView.increaseLvl()
		self.figureView.increasePoint()
		self.setRedraw()

	def decrease(self):
		""" retrocedes the animation one step """
		self.figureView.decreaseLvl()
		self.figureView.decreasePoint()
		self.setRedraw()
	
	def autoAdvance(self):
		""" auto advances the animation """
		self.autoadvance = not self.autoadvance

	def autoRetrocede(self):
		""" auto retrocedes the animation """
		self.autoretrocede = not self.autoretrocede
		
	def updateView(self,levels,cantPoints,start,end):
		""" updates the view with a new set of points and range """
		self.figureView.setLevels(levels,cantPoints,start,end)

		
	def changeAnimFreq(self,animSpeed):
		""" changes the animation speed """
		self.animTime = animSpeed
	
	def render(self,timePassed): 
		""" renders the axis and the figure and updates the animation 
			if 'autoadvance' or 'autoretrocede' are set """
		glLight(GL_LIGHT0, GL_POSITION,  (0, 1.5, 1, 0)) 
	
		if self.display_list is None:   
			# Create a display list
			self.display_list = glGenLists(1)				
			glNewList(self.display_list, GL_COMPILE)

			# render stuff			
			self.figureView.render()
			self.axis.render()			
						
			# End the display list
			glEndList()
			
		else:
			# Render the display list			
			glCallList(self.display_list)
		
		self.acumTime += timePassed
		if ( self.acumTime > self.animTime):
			self.acumTime = 0
			if(self.autoadvance):
				self.increase()
			elif(self.autoretrocede):
				self.decrease()
				
		# Show the screen
		pygame.display.flip()
