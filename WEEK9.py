import pygame, sys
import math
pygame.init()
screen=pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])
sinPoints = []
sinClosePoints = []
cosPoints = []
for x in range(0,640):
    y = int(math.cos(x/640*4*math.pi)*200+240)
    cosPoints.append([x,y])
for x in range(0, 640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
    if (x%2==0):
        sinPoints.append([x, y])
    else:
        sinClosePoints.append([x,y])
for start,end in zip(sinPoints,sinClosePoints):
    pygame.draw.lines(screen, [0, 255, 0], False, (start,end), 2)

pygame.draw.lines(screen, [255, 0, 0], False, cosPoints, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()