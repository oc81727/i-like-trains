import pygame
import numpy as np



def d2(p1, p2):
	return np.sum((p2 - p1) ** 2)


def d(p1, p2):
	return np.sum((p2 - p1) ** 2) ** 0.5



class WorldObject:
	def __init__(self, pos, color):
		self.pos = np.array(pos)
		self.color = np.array(color)

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, self.pos, 5)

	def dist2(self, pos):
		return d2(self.pos, pos)

	def dist(self, pos):
		return self.dist2(pos) ** 0.5


class Square(WorldObject):
	def __init__(self, pos, color, size):
		super().__init__(pos, color)
		self.size = np.array(size)

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, pygame.Rect(*self.pos, *self.size))


	def dist(self, pos):

		# to the left
		if (pos[0] < self.pos[0]):
			if (pos[1] < self.pos[1]):
				return d(pos, self.pos)
			if (pos[1] < self.pos[1] + self.size[1]):
				return self.pos[0] - pos[0]
			return d(pos, self.pos + np.array([0, self.size[1]]))

		# same x
		if (pos[0] < self.pos[0] + self.size[0]):
			if (pos[1] < self.pos[1]):
				return self.pos[1] - pos[1]
			if (pos[1] < self.pos[1] + self.size[1]): # inside square
				return -d(self.pos + self.size * 0.5, pos)
			return pos[1] - self.pos[1] - self.size[1]

		# to the right
		if (pos[1] < self.pos[1]):
			return d(pos, self.pos + np.array([self.size[0], 0]))
		if (pos[1] < self.pos[1] + self.size[1]):
			return pos[0] - self.pos[0] - self.size[0]
		return d(pos, self.pos + self.size)



class Circle(WorldObject):
	def __init__(self, pos, color, radius):
		super().__init__(pos, color)
		self.radius = radius

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, self.pos, self.radius)

	# def dist2(self, pos):
		# return d2(self.pos, pos) - self.radius ** 2

	def dist(self, pos):
		return d(self.pos, pos) - self.radius