import pygame, sys
import math
pygame.init()
screen=pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])
sinPoints = []
cosPoints = []
for x in range(0,640):
	y = int(math.cos(x/640*4*math.pi)*200+240)
	cosPoints.append([x,y])
for x in range(0, 640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
    sinPoints.append([x, y])
pygame.draw.lines(screen, [0, 255, 0], False, sinPoints, 2)
pygame.draw.lines(screen, [255, 0, 0], False, cosPoints, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()