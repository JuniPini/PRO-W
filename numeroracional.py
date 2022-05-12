class NumeroRacional:

    def __init__(self, numerador : int, denominador : int):
        self.__numerador   = numerador
        self.denominador = denominador


    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, nuevo_numerador):
        self.__numerador = nuevo_numerador

    @property
    def denominador(self):
        return self.__denominador


    @denominador.setter
    def denominador(self, nuevo_denominador):

        if nuevo_denominador == 0:
            print("[Error] División infinita")
            exit
        else:
            self.__denominador = nuevo_denominador

    def __add__(self, other):

        numerador   = self.__numerador * other.denominador + other.numerador * self.__denominador
        denominador = self.__denominador * other.denominador

        return NumeroRacional(numerador, denominador)

    def __sub__(self, other):

        numerador   = -self.__numerador * other.denominador + other.numerador * self.__denominador
        denominador = self.__denominador * other.denominador

        return NumeroRacional(numerador, denominador)



    def __mul__(self, other):
        numerador   = self.__numerador * other.numerador
        denominador = self.__denominador * other.denominador

        return NumeroRacional(numerador, denominador)

    def __truediv__(self, other):
        numerador   = self.__numerador * other.denominador
        denominador = self.__denominador * other.numerador

        return NumeroRacional(numerador, denominador)

    def __str__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

fraccion = NumeroRacional(15,0)
print(fraccion)