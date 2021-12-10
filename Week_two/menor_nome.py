def menor_nome(lista):

    lista2 = []
 
    for palavra in lista:
        lista2.append(palavra.lower().strip().capitalize())

    lista3 = []
    lista3 = sorted(lista2)
    print("Lista 3 =",lista3)

    while len(lista3[0]) > len(lista3[1]):
        lista3 = lista3[1:]
    
    return lista3[0]
