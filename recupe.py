class NumComplejo:

    def __init__(self, real:int, imaginario:int):
        
    #Añadimos la información que queremos trabajar.
        self.real = real
        self.imaginario = imaginario

    #Añadimos los getters y los setters.
    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, nuevo_real):
        self._real = nuevo_real
        #if not nuevo_real.isnumeric():
            #return print("[Error] Formato no válido")
        
    @property
    def imaginario(self):
        return self._imaginario

    @imaginario.setter
    def imaginario(self, nuevo_imaginario):
        self._imaginario = nuevo_imaginario
        #if not nuevo_imaginario.isnumeric():
            #return print("[Error] Formato no válido")

    #Método para sumar dos números complejos.
    def __add__(self, nuevo_real, nuevo_imaginario):
        
        return nuevo_real + nuevo_real +","+ nuevo_imaginario + nuevo_imaginario 

    #Métedo para multiplicar por un producto escalar.
    def __mul__(self, nuevo_real, nuevo_imaginario, other):
        
        return other*nuevo_real + "," + other*nuevo_imaginario

    #Método para multiplicar dos números complejos.
    def __mul__(self, nuevo_real, nuevo_imaginario):

        return nuevo_real*nuevo_real - nuevo_imaginario*nuevo_imaginario + "," + nuevo_real*nuevo_real + nuevo_imaginario*nuevo_imaginario

    #Método para restar dos números complejos.
    def __sub__(self, nuevo_real, nuevo_imaginario):

        return nuevo_real-nuevo_real + "," + nuevo_imaginario-nuevo_imaginario

    #Método para dividir dos números complejos.
    def __truediv__(self, nuevo_real, nuevo_imaginario):

        return nuevo_real+nuevo_real/nuevo_real**2+nuevo_imaginario**2 + "," + nuevo_imaginario*nuevo_real - nuevo_real*nuevo_imaginario/nuevo_real**2+nuevo_imaginario**2
        
    def __str__(self):
        return "(" + str(self._real) + "," + str(self._imaginario) + "i)"




