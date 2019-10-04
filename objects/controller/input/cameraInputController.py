import pygame
from pygame.locals import *

from objects.utils.vector3 import Vector3

class CameraInputController(object):
	""" manages the user imput that has to deal with camera movment """
	
	def __init__(self):
		""" constructor """
		self.movementDirection = Vector3()
		self.rotationDirection = Vector3()

	def reset(self):
		""" resets the acumulated movment and rotation values """
		self.rotationDirection.set(0.0, 0.0, 0.0)
		self.movementDirection.set(0.0, 0.0, 0.0)

	def handleKeyboardMotionEvents(self):
		""" handles keyboard events """
		pressed = pygame.key.get_pressed()

		if pressed[K_LEFT]:
			self.rotationDirection.y = +1.0
		elif pressed[K_RIGHT]:
			self.rotationDirection.y = -1.0
		if pressed[K_UP]:
			self.rotationDirection.x = -1.0
		elif pressed[K_DOWN]:
			self.rotationDirection.x = +1.0
			
		if pressed[K_z]:
			self.rotationDirection.z = -1.0
		elif pressed[K_x]:
			self.rotationDirection.z = +1.0   

		if pressed[K_a]:
			self.movementDirection.x = -1.0
		elif pressed[K_d]:
			self.movementDirection.x = +1.0	
		if pressed[K_w]:
			self.movementDirection.z = -1.0
		elif pressed[K_s]:
			self.movementDirection.z = +1.0
		if pressed[K_e]:
			self.movementDirection.y = -1.0
		elif pressed[K_q]:
			self.movementDirection.y = +1.0

		return (self.rotationDirection,self.movementDirection)
			
	def handleMouseEvents(self):
		""" handles mouse events """
		rel = pygame.mouse.get_rel()
		
		if rel[1] < 0:
			self.rotationDirection.x = +0.5
		elif rel[1] > 0:
			self.rotationDirection.x = -0.5

		if rel[0] < 0:
			self.rotationDirection.y = +0.5
		elif rel[0] > 0:
			self.rotationDirection.y = -0.5
		
		return self.rotationDirection

