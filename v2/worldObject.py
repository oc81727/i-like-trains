import pygame
import numpy as np



def d3(p1, p2):
	return np.sum((p2 - p1) ** 2) ** 0.5



class worldObject:
	def __init__(self, pos, color):
		self.pos = np.array(pos)
		self.color = np.array(color)


	def dist(self, pos):
		return d3(pos, self.pos)


class Sphere(worldObject):
	def __init__(self, pos, color, radius):
		super().__init__(pos, color)
		self.radius = radius

	def dist(self, pos):
		return d3(pos, self.pos) - self.radius