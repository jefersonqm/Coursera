def print_matrix(matrix):

    print("Matrix:",len(matrix),"x",len(matrix[0])) 
    
    for n in matrix:
        for m in n:
            print(m, end=" ")
        print()
    return

def symmetry(matrix):
    return len(matrix) == len(matrix[0]) 