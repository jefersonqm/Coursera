def incomodam(n):
    if type(n) != int or n < 1:
        return ""
    else:
        return incomodam(n-1)+"{} \n".format("incomodam"*n)

def elefantes(n):
    if n == 1:
        return " Um elefante incomoda muita gente \n"
    else:
        return elefantes(n-1)+" {} elefantes {}muito mais \n {} elefantes {}muita gente\n".format(n,"incomodam "*n,n,"incomodam ")
        
#if __name__ == "__main__":
#   print(elefantes(5))
#    print(incomodam(1))
#    print(incomodam(-1))
#    print(incomodam(1.5))
