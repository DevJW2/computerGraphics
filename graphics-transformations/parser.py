from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	parser_file = open(fname, "r")
	values = [value.strip('\n') for value in parser_file]
	
	for command in range(len(values)):
		if values[command] == 'line':
			coords = values[command+1].split(" ")
			add_edge(points, int(coords[0]),int(coords[1]),int(coords[2]),int(coords[3]),int(coords[4]),int(coords[5]))

		elif values[command] == 'ident':
			ident(transform)

		elif values[command] == 'scale':
			coords = values[command+1].split(" ")
			scale_matrix = make_scale(int(coords[0]),int(coords[1]),int(coords[2]))
			#print_matrix(scale_matrix)
			matrix_mult(scale_matrix, transform)

		elif values[command] == 'move':
			coords = values[command+1].split(" ")
			trans_matrix = make_translate(int(coords[0]),int(coords[1]),int(coords[2]))
			#print_matrix(trans_matrix)
			matrix_mult(trans_matrix,transform)

		elif values[command] == 'rotate':
			coords = values[command+1].split(" ")
			if coords[0] == 'x':
				rot_matrix = make_rotX(int(coords[1]))
			elif coords[0] == 'y':
				rot_matrix = make_rotY(int(coords[1]))
			else: 
				rot_matrix = make_rotZ(int(coords[1]))
			#print_matrix(rot_matrix)
			matrix_mult(rot_matrix, transform)

		elif values[command] == 'apply':
			matrix_mult(transform, points)

		elif values[command] == 'display':
			for r in range(len(points)):
				for c in range(4):
					points[r][c] = int(points[r][c])
			clear_screen(screen)
			draw_lines(points, screen, color)
			display(screen)

		elif values[command] == 'save':
			draw_lines(points, screen, color)
			save_extension(screen, values[command+1])

		elif values[command] == 'quit':
			break 
	print("Parser Complete")
	parser_file.close()
