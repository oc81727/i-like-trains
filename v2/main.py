import pygame
import numpy as np
import ctypes
from worldObject import *

# ctypes.windll.user32.SetProcessDPIAware() # disable window scaling fr


resolution = np.array([400, 320])


camArray = np.zeros([resolution[0], resolution[1], 3])
deg2Rad = 0.0174533


def norm3d(v):
	invl = 1 / ((v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) ** 0.5)
	return v * invl


window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()



"""
	y     
    |       z
	|     /
	|   /
	| /
	L ------ x

"""




world = set()
world.add(Sphere([8000, -4000, 10000], [0, 0, 0], 2000))

world.add(Sphere([-3000, -6000, 8000], [100, 0, 0], 1500))
world.add(Sphere([2000, 4000, 16000], [0, 0, 100], 3000))



playerPos = np.array([0., 0., 0.])
lookDirection = np.array([0., 0., 1.])
fov = 90
focalLength = (resolution[0] * 0.5) / np.tan(fov*0.5 * deg2Rad)




def march(pos, world):
	far = 99999
	farObj = None
	for obj in world: 
		d = obj.dist(pos)
		if d < far:
			far = d
			farObj = obj
	return far, farObj







running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	window.fill((255, 255, 255))




	topLeft = playerPos + lookDirection * focalLength
	topLeft[0] -= resolution[0] * 0.5
	topLeft[1] += resolution[1] * 0.5

	# print(focalLength)

	camArray = np.zeros([resolution[0], resolution[1], 3])
	for y in range(resolution[1]):
		for x in range(resolution[0]):
			screenPos = topLeft + np.array([x, -y, 0])
			rayDir = norm3d(screenPos - playerPos)

			marchPos = np.copy(playerPos)
			totalDist = 0
			marchNum = 0
			# for i in range(50):
			while True:
				marchNum += 1
				marchDist, closestObj = march(marchPos, world)
				totalDist += marchDist
				if marchDist < 1:
					# camArray[x][y] = closestObj.color
					th = np.tanh(marchNum**4 * 0.00001)
					camArray[x][y] = np.array([255, 255, 255]) * th + closestObj.color * (1-th)
					break
				if totalDist > 20000:
					break


				marchPos += rayDir * marchDist
	# camArray[resolution[1]//2][resolution[0]//2] = np.array([0, 255, 0])
	print("frame done")


	


	pygame.surfarray.blit_array(window, camArray)

	pygame.display.flip()
	clock.tick(60)
