def busca_sequencial(seq, x):
      
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

if __name__ == "__main__":

    seq = [0,1,2,4,5,6,7,8,9,10]
    print(busca_sequencial(seq, 7))    
