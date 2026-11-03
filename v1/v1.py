import pygame
import numpy as np
import ctypes
from worldObject import *

ctypes.windll.user32.SetProcessDPIAware() # disable window scaling fr


resolution = np.array([800, 640])
playerPos = resolution * 0.5
playerColor = np.array([100, 100, 100])
direction = np.array([1, 0])





world = set()
world.add(Square([50, 50], [10, 10, 250], [50, 50]))
world.add(Circle([600, 500], [10, 250, 10], 80))


def norm2d(v):
	return v / ((v[0] * v[0] + v[1] * v[1]) ** 0.5)


def march(pos):
	far = 9999
	for obj in world:
		d = obj.dist(pos)
		if d < far:
			far = d
	return far

window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False



	window.fill((255, 255, 255))


	mousePos = pygame.mouse.get_pos()

	direction = norm2d(mousePos - playerPos)

	pygame.draw.circle(window, [255, 0, 0], playerPos, 5)
	# pygame.display.flip()

	for obj in world:
		obj.draw(window)


	marchPos = np.copy(playerPos)
	for i in range(5):
		far = march(marchPos)
		pygame.draw.circle(window, playerColor, marchPos, far, width = 5)
		marchPos += far * direction
		# input()



	pygame.display.flip()
	clock.tick(60)
