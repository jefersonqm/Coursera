def soma_matrizes(m1, m2):
    #verifica dimensoes
    if dimensoes(m1) != dimensoes(m2):
        return m1 == m2
    #cria matriz que será o resultado da soma
    linha = len(m1)
    coluna = len(m1[0])
    resultado = cria_matriz(linha,coluna,0)
    
    #insere o resultado da soma na matriz criada
    for n in range(linha):
        for m in range(coluna):
            resultado[n][m] = m1[n][m] + m2[n][m]
    return resultado

def dimensoes(minha_matriz):
    #verificar se dimenoes são iguais
    total_linhas = (len(minha_matriz))
    total_colunas = (len(minha_matriz[0]))
    minha_matriz = [total_linhas, total_colunas]
    
    return minha_matriz

def cria_matriz(linha, coluna, valor):  
    #cria matriz vazia
    M3 = []
    
    #cria linha
    for n in range(linha):
        matriz = []        
        for m in range(coluna):
            #insere o valor
            matriz.append(valor)
        
        #adiciona linha na matriz
        M3.append(matriz)

    return M3

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A, B))