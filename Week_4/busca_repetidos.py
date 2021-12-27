def acha_repeticoes(list):
    ''' programa que le uma sequencia com N elementos e a imprime
        sem repeticoes.'''
    
    for n in seq:
        if seq.count(n) > 1:
            seq.remove(n)

    return sorted(seq)
    
if __name__ == "__main__":
    seq = [9,9,3,2,4,8,7,5,5,2,1,3,4,9,0,6]
    print(acha_repeticoes(seq))
    print("seq = [9,9,3,2,4,8,7,5,5,2,1,3,4,9,0,6]")

