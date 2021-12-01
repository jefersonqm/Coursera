def imprima_matriz(matriz):
    '''(matriz) -> None

    Recebe e imprime uma matriz de inteiros.

    >>> a = [[1,2,3],[2,1,4],[3,4,1]]
    >>> a
    [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
    >>> imprima_matriz(a)
    Matriz: 3 x 3
         1     2     3
         2     1     4
         3     4     1
    '''
    for n in matriz:
        for m in n:
            print(m, end=" ")
        print()


# testes
a = [[1,2,3],[2,1,4],[3,7,5],[3,7,5]]
print("Matriz:",len(a[0]),"x",len(a))
imprima_matriz(a)