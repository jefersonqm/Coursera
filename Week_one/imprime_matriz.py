def imprime_matriz(minha_matriz):
    for n in minha_matriz:
        for m in n:
            if m == (n[-1]):
                print(m,end="")
            else:
                print(m,end="-")
        print()
   
