class NumeroRacional():
    
    def __init__(self, numerador, denominador):
        
        #Añadiremos la información con la que vamos a trabajar.

        self.numerador = numerador
        self.denominador = denominador

    #Procedemos a introducir los getters y los setters.
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
        self.__denominador = nuevo_denominador
        if nuevo_denominador == 0: 
          return print("[Error]División infinita")
    
    #Metodo para sumar.
    def __add__(self, nuevo_numerador, nuevo_denominador):
        return nuevo_numerador/nuevo_denominador + nuevo_denominador/nuevo_denominador 

    #Metodo para restar.
    def __sub__(self, nuevo_numerador, nuevo_denominador):
        return nuevo_numerador/nuevo_denominador - nuevo_numerador/nuevo_denominador

    #Metodo para multiplicar.
    def __mul__(self, nuevo_numerador, nuevo_denominador):
        return nuevo_numerador/nuevo_denominador * nuevo_numerador/nuevo_denominador

    #Metodo para dividir.
    def __div__(self, nuevo_numerador, nuevo_denominador):
        return nuevo_numerador/nuevo_denominador / nuevo_numerador/nuevo_denominador