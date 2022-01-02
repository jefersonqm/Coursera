def fatorial(n):
    if n >= 0 and n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

#if __name__ == "__main__":
#    for n in range(10):
#        print(fatorial(n))
