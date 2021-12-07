def ordena_str(lista):
    
    ordem = []
    for n in lista:
        ordem.append(n.lower())
    
    ordem = sorted(ordem)

    return ordem[0]

    