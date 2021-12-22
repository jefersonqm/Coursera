def conta_letras(frase, contar="vogais"):

    lista_vogais = ["a","e","i","o","u","A","E","I","O","U"]
    vogais = []
    consoantes = []
    
    for letras in frase.split():
        for palavras in letras:
            if palavras not in lista_vogais:
                consoantes.append(palavras)
            else:
                vogais.append(palavras)

    if contar == "consoantes":
        return len(consoantes)
    else:
        return len(vogais)
