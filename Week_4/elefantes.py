def incomodam(n):
    if type(n) != int or n < 1:
        return ""
    else:
        return incomodam(n-1)+("incomodam ")

def elefantes(n):
    if n < 2:
        return ""
    else:
        if n > 0 and n < 3:
            return "Um elefante incomoda muita gente\n{} elefantes {}muito mais".format(n,("incomodam "*n))+elefantes(n-1)
        else:
            return elefantes(n-1)+"\n{} elefantes incomodam muita gente\n{} elefantes {}muito mais".format((n-1),n,"incomodam "*n)


            
#if __name__ == "__main__":
#    print(elefantes(4))
#     print(incomodam(1))
#    print(incomodam(-1))
#    print(incomodam(1.5))
    
