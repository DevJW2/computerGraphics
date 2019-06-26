from display import *
from draw import *
from math import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

#TEST

for i in range(36):
    i += 10
    color[0] = random.randint(0,255)
    color[1] = random.randint(0,255)
    color[2] = random.randint(0,255)
    draw_line(XRES/2, YRES/2, XRES/2 + int(cos(i) * 100), YRES/2 + int(sin(i) * 100), screen, color)



display(screen)

save_extension(screen, 'img.png')
