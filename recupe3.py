from abc import ABC, abstractclassmethod


class Alojamiento(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

    def mostrar():
        return "Este es el mostrar de Alojamiento"


class Hotel(Alojamiento):

    def mostrar(self):
        return super().mostrar()

print(Hotel.mostrar())