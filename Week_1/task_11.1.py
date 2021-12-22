def read_matrix():
    '''Function which receive elements and make a matrix.'''

    #insert quantity of lines and columns
    n_lines = int(input("Type the number of lines: "))
    m_columns = int(input("Type the number of columns: "))
    
    #make a matrix
    matrix = []
    
    #make a line
    for n in range(n_lines):
        print("Matrix =",matrix)
        lines = []
        #make a column        
        for m in range(m_columns):
            #get values and insert in line
            value = int(input("Type the number in the position: [" + str(n) + "][" + str(m) + "] = "))
            lines.append(value)
            print("Line", len(matrix)," = ",lines)
        #included line in the matrix
        matrix.append(lines)

    return matrix

a_mat = read_matrix()
print("Matrix =",a_mat)
