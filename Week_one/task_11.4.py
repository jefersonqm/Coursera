def main(matrix):
    for n in matrix:
        print("+---"*len(n))
        for m in n:
            print("|", m ,end=" ")
        print("|")
        
    return