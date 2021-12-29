import random
def lista_grande(n):
    list = []

    for item in range(n):
        list.append(item)

    random.shuffle(list)
    return list

#if __name__ == "__main__":    
#    print(lista_grande(5))
#    print(lista_grande(15))
