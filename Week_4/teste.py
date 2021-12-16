class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return "%d/%d"%(self.numerador, self.denominador)

a = Racional(2, 3)
print(a)
b = Racional(1, 4)
print(b)
