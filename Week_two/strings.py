def mais_curto(lista):
    #função recebe uma lista de strings e retorna a mais curta
    #ignora espaços
    #retorna a string capitalizada
    
    remove_espaços = []
    for palavras in lista:
        remove_espaços.append(palavras.strip())

    ordena_tamanho = []
    ordena_tamanho.append(sorted(remove_espaços, key=len))

    return ordena_tamanho[0]