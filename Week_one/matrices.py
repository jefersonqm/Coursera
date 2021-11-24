def create_matrix(num_rows, num_columns):
    '''(int, int) -> matrix, list of lists'''
    #empty list
    matrix = []

    #create row
    for i in range(num_rows):
        rows = []
        #create columns
        for j in range(num_columns):
            value = int(input("Type number: [" + str(i) + "][" + str(j) + "]")) 
            rows.append(value)
        
        #adds a row to the matrix
        matrix.append(rows)
    
    #changes the format of the function's output
    while len(matrix) > 0:
        print(matrix.pop(0))
 

def read_matrix():
    row = int(input("Type the number de rows of matrix."))
    column = int(input("Type the number de columns of matrix."))
    return create_matrix(row, column)