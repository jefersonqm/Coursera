def mais_curto(lista):
    #Função recebe uma lista de strings.
    #Retorna a palavra com a menor quantidade de caracteres.
    #Ignora espaços.
    #Retorna a string capitalizada

    remove_espaços = []
    for palavras in lista:
        remove_espaços.append(palavras.strip())
        ordena_tamanho = []
        ordena_tamanho.extend(sorted(remove_espaços, key=len))

    return (ordena_tamanho[0].capitalize())