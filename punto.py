import math

class Punto():
    def __init__(self, x= 0, y= 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    def __str__(self):

        return  "(" + str(self.x)+ "x," + str(self.y)+ "y)"

    def cuadrante(self, x, y):
        if x == 0 and y != 0:
            return x and y
        elif x != 0 and y == 0:
            return x and y
        elif x == 0 and y ==0:
            return x and y
        else:
            return print("No entra en los parametros")

    def vector(self, nuevo_punto):

        x = self.x - nuevo_punto.x

        y = self.y - nuevo_punto.y

    def distancia(self, nuevo_punto):

        x = nuevo_punto.x - self.x

        y = nuevo_punto.y - self.y
        
        d = pow(x, 2) + pow(y, 2)

        math.sqrt(d)