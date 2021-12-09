def maiusculas(frase):
    result = ('')
    for l in frase:
	    if ord(l) >= 65 and ord(l) <= 90:
		    result = result + l
    
    return result