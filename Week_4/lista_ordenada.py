def ordenada(lista):

    cont = 1

    while cont < len(lista):
        for n in range(len(lista)-1):
            if lista[n] > lista[cont]:
                return False
            else:
                cont += 1
    return True
        

'''
if __name__ == "__main__":
    lista = [8, 4, 2, 1, 3, 7, 9, 5, 6]
    print(ordenada(lista))
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]
    print(ordenada(lista2))
    lista3 = [3,3,1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(ordenada(lista3))
    lista3 = [3,3,9,7,1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(ordenada(lista3))
    lista3 = [3,3,9,7,2, 3, 4, 5, 6, 7, 8, 9,1]
    print(ordenada(lista3))
'''
