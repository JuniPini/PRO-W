from Persona import Persona


'''dinero = 0

total = []

class Cuenta:
    
    def __init__(self,titular, dinero):
        self.titular = titular
        self.dinero = dinero
        
    @property
    def titular(self):
        return self.titular
    
    @titular.setter
    def titular(self, nuevo_nombre):
        self.titular = nuevo_nombre

    def mostrar(self):
        return 'Titular: ' + self.titular + 'Dinero: €' + str(self.dinero)
    
    def ingresar(self, cantidad):
        cantidad = int(input("Introduce la cantidad a ingresar: "))
        self.dinero += total

    def retirar(self, cantidad):
        cantidad = int(input("Introduce la cantidad a retirar: "))
        if total < cantidad:
            print("No tienes suficientes fondos")
        else:
            print("Se ha retirado " + cantidad + "de tu cuenta.")
    

    
persona1 = Cuenta()

persona1.titular = "Junior"
persona1.dinero = 10

print(persona1.mostrar())'''




class Cuenta:
    
    def __init__(self,titular, cantidad = 0.):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    
    def mostrar(self):
        return self.__titular.mostrar() + "Cantidad: " + str(self.__cantidad)

    def ingresar(self, cantidad_ingreso):
        if cantidad_ingreso > 0:
            self.__cantidad = self.__cantidad + cantidad_ingreso
    
    def retirar(self, cantidad_retiro):
        self.__cantidad = self.__cantidad -cantidad_retiro


persona = Persona('Juan Rafael',36,'72342342')

p2 = Persona("Pepe", "García", "Pinillos", 23, '78819396')
cuenta = Cuenta(p2,1000)


print(cuenta.mostrar())

cuenta.ingresar(2000)

print(cuenta.mostrar())

cuenta.retirar(1000)

print(cuenta.mostrar())


'''from persona import Persona


class Cuenta:

    def __init__(self, titular : Persona, cantidad : float = 1000):

        self.__persona  = titular
        self.__cantidad = cantidad


    @property
    def persona(self):
        return self.__persona

    @persona.setter
    def persona(self, nueva_persona):
        self.__persona = nueva_persona

    @property
    def cantidad(self):
        return self.__cantidad
        
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad



    def mostrar(self):
        return self.__persona.mostrar() + " Cantidad: " + str(self.__cantidad)


    def ingresar(self, cantidad=0):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad = 0):
        self.__cantidad = self.__cantidad - cantidad'''