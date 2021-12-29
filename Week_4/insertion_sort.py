def insertion_sort(lista):

    i = 1
    fim = len(lista)
    nova_lista = []


    while i < fim:
        item = lista[i]
        j = i
        i += 1

        while (j > 0 and lista[j - 1] > item):
            lista[j] = lista[j - 1]
            j -= 1

        lista[j] = item

    i = 0
    while i < fim:
        nova_lista.append(lista[i])
        i += 1

    return nova_lista
