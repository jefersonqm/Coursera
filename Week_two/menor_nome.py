def menor_nome(lista):

    lista2 = []
 
    for palavra in lista:
        lista2.append(palavra.lower().strip())

    lista3 = []
    lista3 = sorted(lista2)

    if len(lista3[0]) <= len(lista3[1]):
        return lista3[0]
    else:
        return lista3[1]

