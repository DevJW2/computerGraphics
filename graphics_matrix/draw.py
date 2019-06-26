from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for p in range(0, len(matrix[0]), 2):
        draw_line(matrix[0][p], matrix[1][p], matrix[0][p+1], matrix[1][p+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap
    if x1 < x0: 
        draw_line(x1, y1, x0, y0, screen, color)


    x = x0
    y = y0 
    a = y1 - y0
    b = x0 - x1

    if (b == 0):
        if (y < y1):
            while(y <= y1):
                plot(screen, color, x, y)
                y = y + 1
        if (y > y1):
            while(y1 <= y):
                plot(screen, color, x, y)
                y = y - 1
        return

    #slope 
    m = float(a)/float(-1 * b)

    #OCTANT 1
    if m >= 0 and m <= 1: 
        d = 2 * a + b
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    #OCTANT 2
    elif m > 1: 
        d = a + 2 * b
        while y <= y1:
            plot(screen,color, x, y)
            if d < 0:
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
    #OCTANT 7
    elif m < -1: 
        d = a - 2 * b
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0: 
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * b
    #OCTANT 8
    elif m >= -1:
        d = 2 * a - b
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0: 
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a