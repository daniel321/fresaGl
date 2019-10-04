import pygame
from math import radians

from OpenGL.GL import *
from OpenGL.GLU import *

from objects.utils.matrix44 import Matrix44
from objects.utils.vector3 import Vector3

from cameraInputController import CameraInputController 

class CameraController(object):
	""" manages the camera """
	
	def __init__(self):	
		""" initializes the camera """
		self.resetCamera()
		self.cameraInputController = CameraInputController()
		
	def resetCamera(self):
		""" sets the camera to the default position """
		self.camera_matrix = self.startMatrix = Matrix44([ 0.856094182898, -0.2309159205410, 0.365667875051, 0.0],
														 [ 0.334274233642,  0.9681386883340, 0.178622224799, 0.0],
														 [-0.407209784594, -0.0968778498464, 0.913444637602, 0.0],
														 [ 3.353325164320,  2.4798717299300, 17.79564977640, 1.0] )

		self.rotationSpeed = 2.0
		self.movementSpeed = 10.0
		self.clock = pygame.time.Clock()	
	
	def handleCameraEvents(self):
		""" handles keyboard and mouse events """	
		self.cameraInputController.reset()
		(rotationDirection,movementDirection) = self.cameraInputController.handleKeyboardMotionEvents()
		# rotationDirection = self.cameraInputController.handleMouseEvents()
			
		return (rotationDirection,movementDirection)
	
	def updateCamera(self,timePassed):
		""" updates the camera matrix"""
		(rotationDirection,movementDirection) = self.handleCameraEvents()
	
		# rotation
		rotation = rotationDirection * self.rotationSpeed * timePassed
		rotation_matrix = Matrix44.xyz_rotation(*rotation)		
		self.camera_matrix *= rotation_matrix
		
		# translation
		heading = Vector3(self.camera_matrix.forward)
		movement = heading * movementDirection.z * self.movementSpeed					
		self.camera_matrix.translate += movement * timePassed

		heading = Vector3(self.camera_matrix.up)
		movement = heading * movementDirection.y * self.movementSpeed					
		self.camera_matrix.translate += movement * timePassed
		
		heading = Vector3(self.camera_matrix.up).cross(Vector3(self.camera_matrix.forward))
		movement = heading * movementDirection.x * self.movementSpeed					
		self.camera_matrix.translate += movement * timePassed

		# num = 0
		# for point in self.camera_matrix:
			# print str(point),
			# if(num == 3):
				# print
			# num = (num+1)%4
		# print 
		
		# Upload the inverse camera matrix to OpenGL
		glLoadMatrixd(self.camera_matrix.get_inverse().to_opengl())

