import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    polygons = []
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = [] 
    edges = []
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        for args in commands:
            if args[0] != "rotate" and args[0] != "save" and args[0] != "display":
                temp = [args[0]]
                for value in args[1:]:
                    if isinstance(value, float):
                        temp.append(value)
                args = tuple(temp)

            line = args[0]
            if line == 'sphere':
                #print 'SPHERE\t' + str(args)
                add_sphere(polygons,
                            float(args[1]), float(args[2]), float(args[3]),
                            float(args[4]), step_3d)
                matrix_mult( stack[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
            elif line == 'torus':
                #print 'TORUS\t' + str(args)

                add_torus(polygons,
                        float(args[1]), float(args[2]), float(args[3]),
                        float(args[4]), float(args[5]), step_3d)
                matrix_mult( stack[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
                
            elif line == 'box':
                #print 'BOX\t' + str(args)

                add_box(polygons,
                        float(args[1]), float(args[2]), float(args[3]),
                        float(args[4]), float(args[5]), float(args[6]))
                matrix_mult( stack[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []

            elif line == 'line':
                #print 'LINE\t' + str(args)
                add_edge( edges,
                        float(args[1]), float(args[2]), float(args[3]),
                        float(args[4]), float(args[5]), float(args[6]) )
                matrix_mult( stack[-1], edges )
                draw_lines(edges, screen, zbuffer, color)
                edges = []

            elif line == 'scale':
                #print 'SCALE\t' + str(args)
                t = make_scale(float(args[1]), float(args[2]), float(args[3])) #check this
                matrix_mult( stack[-1], t )
                stack[-1] = [ x[:] for x in t]

            elif line == 'move':
                #print 'MOVE\t' + str(args)
                t = make_translate(float(args[1]), float(args[2]), float(args[3]))
                matrix_mult( stack[-1], t )
                stack[-1] = [ x[:] for x in t]

            elif line == 'rotate':
                #print 'ROTATE\t' + str(args)
                theta = float(args[2]) * (math.pi / 180)
                if args[1] == 'x':
                    t = make_rotX(theta)
                elif args[1] == 'y':
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult( stack[-1], t )
                stack[-1] = [ x[:] for x in t]

            elif line == 'push':
                stack.append( [x[:] for x in stack[-1]] )

            elif line == 'pop':
                stack.pop()

            elif line == 'display' or line == 'save':
                 if line == 'display':
                    display(screen)
                 else:
                    save_extension(screen, args[1] + args[2]) #fix this
                
    else:
        print ("Parsing failed.")
        return
