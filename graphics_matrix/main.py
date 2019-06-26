from display import *
from draw import *
from matrix import *
from math import *
import random

screen = new_screen()
color = [ 0, 203, 223]

test_matrix = new_matrix()

print("---Testing print_matrix---")
print_matrix(test_matrix)
print("---Testing identity matrix---")
print_matrix(ident(test_matrix))

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print("---Testing matrix multiplication---\n")
print("Matrix 1:  [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]\n")

print("Matrix 1 * Matrix 1")
matrix_mult(matrix1, matrix1)

print("Matrix 1 * Identity")
matrix_mult(matrix1, ident(test_matrix))

matrix_points = new_matrix(4,0)

print("---Testing add_point---\n")
add_point(matrix_points, 4, 5)
add_point(matrix_points, 6, 9)
add_point(matrix_points, 3, 11)
add_point(matrix_points, 7, 2)

print_matrix(matrix_points)

matrix_edges = new_matrix(4,0)

print("---Testing add_edge---\n")
add_edge(matrix_edges, 1, 3, 0, 5, 7, 0)
add_edge(matrix_edges, 4, 4, 0, 7, 9, 0)

print_matrix(matrix_edges)

print("--DRAWING LINES---\n")
matrix = new_matrix(4,0)

def square(x0, y0, x1, y1, x2, y2, x3, y3):
    add_edge(matrix, x0, y0, 0, x1, y1, 0)
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    add_edge(matrix, x2, y2, 0, x3, y3, 0)
    add_edge(matrix, x3, y3, 0, x0, y0, 0)


square(0, 0, 0, 50, 83, 50, 83, 0)
square(83, 0, 83, 150, 166, 150, 166, 0)
square(166, 0, 166, 300, 249, 300, 249, 0)
square(249, 0, 249, 400, 332, 400, 332, 0)
square(285,400, 285, 480, 295, 480, 295, 400)
square(332, 0, 332, 230, 415, 260, 415, 0)
square(415, 0, 415, 200, 500, 200, 500, 0)


for i in range(36):
    i += 10
    add_edge(matrix, XRES/2 - 150, YRES/2 + 150, 0, XRES/2 - 150 + int(cos(i) * 100), YRES/2 + 150 + int(sin(i) * 100), 0)







draw_lines( matrix, screen, color )
display(screen)

save_extension(screen, 'img.png')
