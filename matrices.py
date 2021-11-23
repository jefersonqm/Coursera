def create_matrix(num_rows, num_columns, value):
    '''(int, int, value) -> matrix, list of lists'''
    #empty list
    matrix = []

    #create row
    for i in range(num_rows):
        rows = []
        #create columns
        for j in range(num_columns):
            rows.append(value)
        
        #adds a row to the matrix
        matrix.append(rows)
    
    #changes the format of the function's output
    while len(matrix) > 0:
        print(matrix.pop(0))