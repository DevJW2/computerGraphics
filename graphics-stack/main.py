from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []

transform = new_matrix()
ident(transform)
cs_stack = []
cs_stack.append(transform)

parse_file( 'galleryScript', edges, polygons, cs_stack, screen, color )
