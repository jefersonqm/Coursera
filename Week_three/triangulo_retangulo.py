class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a != self.b and self.b != self.c and self.a != self.c: 
            return "escaleno"
        elif self.a == self.b and self.b == self.c:
            return "equilátero"
        else:
            return "isósceles"
    
    def retangulo(self):
        quadrado_catetos = self.a**2 + self.b**2 
        quadrado_hipotenusa = self.c**2

        return quadrado_catetos == quadrado_hipotenusa

    def semelhante(triangulo):
        triangulo = Triangulo()
        
        return


