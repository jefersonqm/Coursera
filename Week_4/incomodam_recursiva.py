<<<<<<< HEAD
def incomdomam(n):
    if not int > 0:
        return " " * n
    else:
        "incomodam" * n
=======
def incomodam(n):
    if type(n) != int or n < 1:
        return ""
    else:
        return incomodam(n)

def elefantes(n):
    if n <= 1 or type(n) != int:
        return ""
    else:
        return elefantes(n-1)+" Um elefante incomda muita gente \n {} elefantes {} muito mais\n".format(n,'incomodam '*n)
        
#if __name__ == "__main__":
#    print(elefantes(10))
#    print(elefantes(1))
#    print(elefantes(-1))
#    print(elefantes(1.5))
>>>>>>> da2322a1d72d15c4810d10d5ed672a744566fc56
