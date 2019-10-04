import pygame
from pygame.locals import *

from objects.utils.paths import Paths

from objects.utils.matrix44 import Matrix44
from objects.utils.files.pathLoader import PathLoader 
from objects.utils.files.codeSaver import CodeSaver

from objects.model.model import Model

from objects.controller.launchers.launcherController import LauncherController

from objects.view.window2D.popups.helpMessage import HelpMessage
from objects.view.window2D.popups.inputAsker import InputAsker

class EventController(object):
	""" main controller for the program """
	
	def __init__(self):	
		""" constructor """
		self.model = None
		self.quit = False
		self.showOnlySelection = True

		self.setAllVariables(0,999999,-1,-1)	
			
	def initialize(self,view,cameraController,actionWindow,codeWindow):
		""" initializes the main controller """
		self.cameraController = cameraController		
		self.view = view
		self.actionWindow = actionWindow	
		self.codeWindow = codeWindow	

		self.launcherController = LauncherController(view,codeWindow,actionWindow)	
	
	def setAllVariables(self,start,end,tolerance,feedRate):
		""" sets all configurable variables """
		self.editStart = start
		self.editEnd   = end	

		self.tolerance = tolerance
		self.feedRate  = feedRate				

	def askNewRange(self):
		""" asks the user for the new range and changes it """
		if(self.model):
			asker = InputAsker()
			(start,end) = asker.askNewRange((self.editStart,self.editEnd))

			if( (start,end) != (None,None) ):
				self.setRange(start,end)	
	
	def setRange(self,start,end):
		""" changes the selected range """	
		if(self.model):		
			code = self.model.getModifiedGCode()
			tempPath = Paths.Instance().tempPath
			CodeSaver().save(code,tempPath)
			
			self.setAllVariables(start,end,-1,-1)

			self.model.changePath(tempPath)	
			self.view.updateView(self.model.getLevels(),self.model.getCantPoints(),start,end)
		
			self.actionWindow.updateSliderPos(start,end)
			
			self.updateCodeWindow()			
			self.view.setRedraw()
	
	def updateCodeWindow(self):
		""" updates the code displayed in the window to reflect the selection """
		""" if 'showOnlySelection' is false displays all the code """
		code = self.model.getModifiedGCode()
		self.codeWindow.update(code,self.editStart,self.editEnd)

	def askNewTolerance(self):
		""" asks the user for the new tolerance and changes it """
		if(self.model):
			tol = InputAsker().askNewTolerance(self.tolerance)
			if(tol):
				self.setTolerance(tol)
		
	def setTolerance(self,tolerance):
		""" changes the tolerance and adds intermediate points acordingly """
		self.tolerance = tolerance
		self.calculateModel()
	
	def askNewVel(self):
		""" asks the user for the new vel and changes it """
		if(self.model):
			vel = InputAsker().askNewVel(self.feedRate)
			if(vel):
				self.setFeedRate(vel)		
		
	def setFeedRate(self,feedRate):
		""" changes the feedRate and edits the G-code acordingly """
		self.feedRate = feedRate
		self.calculateModel()

	def loadNewModel(self):
		""" loads a new model from a G-code file """
		path = PathLoader().loadPath()
		if(path):
			self.cameraController.resetCamera()	
			self.setAllVariables(0,999999,-1,-1)						
			self.loadModel(path)	
		
	def loadModel(self,path):
		""" reloads the model from the current G-code file """
		self.model = Model(path)
		
		self.calculateModel()
		self.cameraController.resetCamera()
		
	def calculateModel(self):
		""" updates the model and applies the different parsers 
			to generate the modified G-code and the list of points """
		if (self.model):
			self.model.generateModel([0,0,0,-1],self.editStart,self.editEnd,self.tolerance,self.feedRate)
			
			(start,end) = self.model.getFinalRange()	

			self.actionWindow.updateSliderRange(0,self.model.getCantLines())			
			self.actionWindow.updateSliderPos(start,end)
			
			self.view.updateView(self.model.getLevels(),self.model.getCantPoints(),start,end)
			self.view.setRedraw()
			self.updateCodeWindow()	
		
	def launchMach3(self):
		""" launches mach3 with the modifyed code """
		if(self.model):
			self.launcherController.launchMach3(self.model.getModifiedGCode())
			self.cameraController.resetCamera()	

	def launchTextEditor(self):
		""" launches the text editor with the code selected and merges it back together afterwards """
		if(self.model):		
			(start,end) = self.launcherController.launchTextEditor(self.model.getModifiedGCode(),self.editStart,self.editEnd)
			self.loadModel(Paths.Instance().tempPath)
			self.setRange(start,end)			
			
			self.cameraController.resetCamera()	

	def showHelpMessage(self):
		""" displays the 'help' message """
		HelpMessage().showHelpMessage()	
			
	def selNextLvl(self):
		""" selects the next level """
		if (self.model):
			self.setViewMode(0)

			(start,end) = self.model.getNextLvl(self.editStart)
			self.setRange(start,end)
		
	def selPrevLvl(self):
		""" selects the previous level """
		if (self.model):
			self.setViewMode(0)

			(start,end) = self.model.getPrevLvl(self.editStart)
			self.setRange(start,end)
	
	def retrocedeView(self):
		""" retrocedes the animation once """
		self.view.decrease()
		
	def advanceView(self):	
		""" advances the animation once """
		self.view.increase()
	
	def autoAdvanceView(self):
		""" auto advances the animation """
		self.view.autoAdvance()
	
	def autoRetrocedeView(self):
		""" auto retrocedes the animation """
		self.view.autoRetrocede()
	
	def resetView(self):
		""" resets the animation """
		self.view.resetView(self.editStart)			
	
	def changeViewShape(self):
		""" changes the shape to be drawn (both,points,lines) """
		self.view.changeViewShape()

	def setViewShape(self,shapeNum):
		""" determines the shape to be drawn (both,points,lines) """
		self.view.setViewShape(shapeNum)

	def changeViewMode(self):
		""" changes the drawing mode (all,by levels,by points) """
		self.view.changeViewMode()	

	def setViewMode(self,mode):
		""" determines the drawing mode (all,by levels,by points) """
		self.view.setViewMode(mode)	
		
	def changeAnimFreq(self,freq):
		""" changes the animation speed """
		self.view.changeAnimFreq(freq)
		
	def toggleShowOnlySelection(self):
		""" determines weather if all the figure 
			will be shown or only the selected area """
		if (self.model):
			self.view.toggleShowOnlySelection(self.editStart)
			self.codeWindow.toggleShowOnlySelection()
			self.updateCodeWindow()
			self.view.setRedraw()
	
	def close(self):
		""" ends the program """
		self.quit = True
	
	def timeToQuit(self):
		""" returns weather if its time to close the program or not """
		return self.quit
