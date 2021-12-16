def mat_mul (A, B):
    num_linhas_A,num_colunas_A = len(A),len(A[0]) 
    num_linhas_B,num_colunas_B = len(B),len(B[0])

    #Verificação da Condição de existência
    #Número de colunas da primeira matriz
    #Precisa ser igual ao número de linhas da segunda matriz
    assert num_colunas_A == num_linhas_B

    C = []
    for linha in range(num_linhas_A):
        #Começando um nova linha vazia.
        C.append([]) 
        for coluna in range(num_colunas_B):
            #Adicionando um nova coluna na linha
            C[linha].append(0) 
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna] 

    #Formata a saída, visualização como tabela.
    for linha in C:
        for coluna in linha:
            print(coluna,end='\t')
        print()    
    return 

#Testes.
if __name__ == '__main__':
    A,B = [[3,2],[5,-1]], [[6,4,-2],[0,7,1]]
    print("Primeiro teste: ")
    mat_mul (A,B)
    print(end="\n")

    A,B = [[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]]
    print("Segundo teste: ")
    mat_mul (A,B)
    