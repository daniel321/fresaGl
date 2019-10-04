import pygame
from pygame.locals import *

class KeyboardController(object):
	""" main controller for the program """
	
	def __init__(self,controller):	
		""" constructor """
		self.controller = controller
			
	def handleKeyboardActionEvents(self):
		""" handles keyboard shorcuts """
		
		for event in pygame.event.get():
			if (event.type == QUIT or event.type == KEYUP) and event.key == K_ESCAPE:
				self.controller.close()
				
			elif event.type == KEYUP and event.key == K_RETURN:
				self.controller.launchMach3()
			elif event.type == KEYUP and event.key == K_SPACE:
				self.controller.loadNewModel()
				
			elif event.type == KEYUP and event.key == K_1:
				self.controller.resetView()		
			elif event.type == KEYUP and event.key == K_2:
				self.controller.changeViewShape()			
			elif event.type == KEYUP and event.key == K_3:
				self.controller.changeViewMode()				
			
			elif event.type == KEYUP and event.key == K_KP_ENTER:
				self.controller.launchTextEditor()

			elif event.type == KEYDOWN and event.key == K_o:
				self.controller.advanceView()
			elif event.type == KEYDOWN and event.key == K_i:
				self.controller.retrocedeView()
				
			elif event.type == KEYDOWN and event.key == K_l:
				self.controller.autoAdvanceView()
			elif event.type == KEYDOWN and event.key == K_k:
				self.controller.autoRetrocedeView()
	
			elif event.type == KEYUP and event.key == K_KP0:
				self.controller.resetView()	
				
			elif event.type == KEYDOWN and event.key == K_KP1:
				self.controller.askNewVel()
			elif event.type == KEYDOWN and event.key == K_KP2:
				self.controller.askNewTolerance()
			elif event.type == KEYDOWN and event.key == K_KP3:
				self.controller.askNewRange()	
				
			elif event.type == KEYDOWN and event.key == K_KP4:
				self.controller.retrocedeView()
			elif event.type == KEYDOWN and event.key == K_KP5:
				self.controller.autoAdvanceView()
			elif event.type == KEYDOWN and event.key == K_KP6:
				self.controller.advanceView()	

			elif event.type == KEYDOWN and event.key == K_KP7:
				self.controller.selPrevLvl()
			elif event.type == KEYDOWN and event.key == K_KP9:
				self.controller.selNextLvl()	
	
			elif event.type == KEYDOWN and event.key == K_F1: 
				self.controller.showHelpMessage()
	
			elif event.type == KEYDOWN and event.key == K_KP_PLUS:
				self.controller.autoAdvanceView()
			elif event.type == KEYDOWN and event.key == K_KP_MINUS:
				self.controller.autoRetrocedeView()