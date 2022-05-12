
from cuenta import Cuenta
from Persona import Persona


class CuentaJoven(Cuenta):

    def __init__(self, titular: Persona, cantidad: float = 500, bonificacion: int = 10):
        super().__init__(titular, cantidad)

        self.__bonificacion = bonificacion


    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion


    def esTitularValido(self):
        return self.persona.esMayorDeEdad() and self.persona.edad < 25


    def retirar(self, cantidad = 0):
        if self.esTitularValido():
            super().retirar(cantidad)


    def mostrar(self):
        return super().mostrar() + " Bonificacion: " + str(self.__bonificacion)