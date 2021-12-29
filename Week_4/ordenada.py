def ordena(lista):
    for passagem in range(len(lista)-1,0,-1):
        maior = 0
        for posicao in range(1,passagem + 1):
            if lista[posicao] > lista[maior]:
                maior = posicao
        
        temp = lista[passagem]
        lista[passagem] = lista[maior]
        lista[maior] = temp 
    
    return lista

#lista = [9,1,2,4,6,5,7,8,10,3]
#ordenada(lista)
#print(lista)
