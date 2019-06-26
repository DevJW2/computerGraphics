import math


def print_matrix( matrix ):
    for r in matrix:
        for c in r:
            print(c),
        print("")
    print("")
    pass

def ident( matrix ):
    counter = 0
    for r in matrix:
        r[counter] = 1
        counter += 1
    
    return matrix

#m1 * m2 -> m2

def matrix_mult( m1, m2 ):
    product = new_matrix()

    total = 0
    counter1 = 0
    counter2 = 0

    for i in range(4):
        for r in range(4):
            for n in range(4):
                total += m1[counter2][n] * m2[n][counter1]
                
            counter1 += 1
            product[counter2][r] = total
            
            total = 0
            
        counter2 += 1
        counter1 = 0
                
    for x in range(4):
        for y in range(4):
            m2[x][y] = product[x][y]
    print_matrix(m2)
    return m2




def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
