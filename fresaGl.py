import pygame
from pygame.locals import *	

import logging
import ConfigParser
import os
import threading

from objects.controller.eventController import EventController
from objects.controller.input.cameraController import CameraController
from objects.controller.input.keyboardController import KeyboardController

from objects.view.window3D.window3d import Window3d	
from objects.view.window2D.actionWindow.actionWindow import ActionWindow 
from objects.view.window2D.codeWindow.codeWindow import CodeWindow 

from objects.utils.paths import Paths

class FresaGl(object):
	""" main program """

	def __init__(self):	
		""" initializes all windows"""	
		logging.basicConfig()
		self.loadConstants()
		
		self.controller = EventController()	
		self.keyboardController = KeyboardController(self.controller)		
		self.cameraController = CameraController()

		self.initWindows()
		
		self.controller.initialize(self.view,self.cameraController,self.actionWindow,self.codeWindow)
	
	def loadConstants(self):
		""" loads program constants (paths & window size percentages)"""
		config = ConfigParser.ConfigParser()
		config.read('paths.cfg')

		workingDir = os.getcwd().replace('\\','/')
		Paths.Instance().savePath =  workingDir + "/output.NC"
		Paths.Instance().tempPath =  workingDir + "/temp.NC"
		Paths.Instance().iconPath =  workingDir + "/resources/"
		
		Paths.Instance().macroPath = config.get('Paths', 'mach3ProfilePath', 0) + "/M777.m1s"
		Paths.Instance().textEditorPath = config.get('Paths', 'textEditorPath', 0)
		Paths.Instance().mach3Path = config.get('Paths', 'mach3Path', 0)
		
		config.read('windowsPercentage.cfg')
		self.height3dWindow = config.getfloat('SizesPercentage', 'height3dWindow')
		self.heightActionWindow = config.getfloat('SizesPercentage', 'heightActionWindow')
		self.width3dWindow = config.getfloat('SizesPercentage', 'width3dWindow')
		self.widthCodeWindow = config.getfloat('SizesPercentage', 'widthCodeWindow')		
	
	def initWindows(self):
		""" initializes the program windows """
		pygame.init()		
		infoObject = pygame.display.Info()
		width = infoObject.current_w
		height = infoObject.current_h

		height1 = int(height*self.height3dWindow)
		height2 = int(height*self.heightActionWindow)

		width1 = int(width*self.width3dWindow)
		width2 = int(width*self.widthCodeWindow)

		self.view = Window3d(width1,height1,(0,0))
		self.view.initView()

		self.codeWindow = CodeWindow(width2,height1,(width1,0))
		self.codeWindow.initialize()
		self.launchWindow(self.codeWindow)
	
		self.actionWindow = ActionWindow(width,height2,(0, height1))
		self.actionWindow.initialize(self.controller)
		self.launchWindow(self.actionWindow)		

	def launchWindow(self,window):
		""" initializes the window in other thread """
		thread = threading.Thread(target=window.MainLoop)
		thread.daemon = True
		thread.start()
	
	def run(self):
		""" main loop """
		clock = pygame.time.Clock()	
		self.cameraController.resetCamera()
	
		while (not self.controller.timeToQuit()):  
			self.step(clock)
	
	def step(self,clock):
		""" single step for the main loop """
		self.view.clearScreen()
		self.keyboardController.handleKeyboardActionEvents()	
			
		timePassed = clock.tick() / 1000.
		self.cameraController.updateCamera(timePassed)	
		self.view.render(timePassed)	
		
program = FresaGl()
program.run()

