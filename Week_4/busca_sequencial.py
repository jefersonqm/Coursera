def busca(lista, elemento):
      
    for i in range(len(lista)):
        if lista[i] == elemento:
            return(i) 
    return False

#if __name__ == "__main__":

#    seq = [0,1,2,4,5,6,7,8,9,10]
#    print(busca(seq, 7))    
