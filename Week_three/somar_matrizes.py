def cria_matrix(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)

    return matriz

def mult_matrizes(A, B):
    num_lin = len(A[0])
    num_col = len(B)
    C = cria_matrix(num_lin, num_col, 0)

    if existencia(A, B) == False:
        print("Condição de existência = ", False)
        return

    for lin in range(num_lin):
        for col in range(num_col):
            C[lin][col] = A[lin][col] * B[lin][col]
    
    for n in C:
        for m in n:
            print(m, end="\t")
        print()
    
    return

def existencia(A, B):
    col_primeira = len(A[0])
    lin_segunda = len(B)

    return col_primeira == lin_segunda