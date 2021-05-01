import pygame
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
            x1, y1 = start_pos
            x2, y2 = end_pos
            dl = dash_length

            if (x1 == x2):
                  ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
                  xcoords = [x1] * len(ycoords)
            elif (y1 == y2):
                  xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
                  ycoords = [y1] * len(xcoords)
            else:
                  a = abs(x2 - x1)
                  b = abs(y2 - y1)
                  c = round(math.sqrt(a**2 + b**2))
                  dx = dl * a / c
                  dy = dl * b / c
                  xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
                  ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

            next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
            last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
            print(last_coords)
            print("last")
            print(next_coords)
            for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
                  start = (round(x1), round(y1))
                  end = (round(x2), round(y2))
                  pygame.draw.line(surf, color, start, end, width)

def create_background(width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background, 
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('press space to see next demo')
background = create_background(width, height)

while True:
      screen.blit(background,(0,0))
      draw_dashed_line(screen,(255,255,0), (0,320),(480,320),width=5)
      pygame.display.flip()