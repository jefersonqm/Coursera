def encontra_impares(lista):

    if len(lista) <= 0:
        return[]
    else:
        impares = []
        if lista[0] % 2 != 0:
            impares.extend([lista[0]])
        return impares + encontra_impares(lista[1:])
        
        


'''if __name__ == "__main__":
    lista = [1,2]
    print(encontra_impares(lista))s
'''
