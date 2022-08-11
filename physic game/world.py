import pygame as pg
import pymunk as pm
from multiprocessing import Process
class World(pg.Surface, Process):


	def __init__(self, width, height, camera, color=[250,250,250]):

		super().__init__([width, height])
		self.width 					= width
		self.height 				= height
		self.color 					= color
		self.camera 				= camera

		self.free_props				= []

		self.shape_being_dragged 	= None

		self.ground_y 				= self.height - 2
		self.Poly = True 
		self.Circle = False
		self.Line = False

		self.mass, self.r = 10,15
		self.ball_mass, self.ball_rad = 50, 60
		self.line_mass, self.line_dli, self.line_rad = 35, 100, 10





	def fill_me(self):

		self.fill(self.color)

	def blit_me(self):
		
		self.camera.blit(self, [0,0])

	def pick_free_prop(self, space, mouse_pos):

		
		query_info = space.point_query_nearest(mouse_pos, 0, pm.ShapeFilter())
		if query_info != None:

			if query_info.shape.collision_type == 0:

				self.shape_being_dragged = query_info.shape

	def release_picked_prop(self):

		self.shape_being_dragged = None

	def move_picked_prop(self, mouse_pos):

		if self.shape_being_dragged != None:

			if mouse_pos[1] < self.ground_y:
				self.shape_being_dragged.body.position = mouse_pos
				self.shape_being_dragged.body.velocity = 0,0