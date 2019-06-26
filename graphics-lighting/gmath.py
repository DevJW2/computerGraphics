from math import *
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    color = [0, 0, 0]
    theAmb = calculate_ambient(ambient, areflect)
    theDiff = calculate_diffuse(light, dreflect, normal)
    theSpec = calculate_specular(light, sreflect, view, normal)
    for index in range(len(color)): 
        color[index] = theAmb[index] + theDiff[index] + theSpec[index]
    return limit_color(color)

def calculate_ambient(alight, areflect):
    color = [0, 0, 0]
    for index in range(len(color)):
        color[index] = alight[index] * areflect[index]
    return limit_color(color)

def calculate_diffuse(light, dreflect, normal):
    color = [0, 0, 0]
    for index in range(len(color)):
        color[index] = light[COLOR][index] * dreflect[index] * dot_product(normalize(light[LOCATION]), normalize(normal))
    return limit_color(color)

def calculate_specular(light, sreflect, view, normal):
    color = [0, 0, 0]
    ltmp = [0, 0, 0]
    cons = 2 * dot_product(light[LOCATION], normal)
    for index in range(len(ltmp)): 
        ltmp[index] = 2 * cons * normal[index] - light[LOCATION][index]
    cons = (dot_product(ltmp, view)) ** 16
    for index in range(len(color)):
        color[index] = color[index] * sreflect[index] * cons
    return limit_color(color)

def limit_color(color):
    for value in range(len(color)): 
        color[value] = int(color[value])
        if color[value] > 255:
            color[value] = 255
        elif color[value] < 0: 
            color[value] = 0
    return color

#vector functions
def normalize(vector):
    magnitude = sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector[0] /= magnitude
    vector[1] /= magnitude
    vector[2] /= magnitude

    return vector
    
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
