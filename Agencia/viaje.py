from aeropuerto import Aeropuerto
from avion import Avion

class Viaje:
    def __init__(self, origen:Aeropuerto, destino:Aeropuerto, avion:Avion):
        self.__origen = origen
        self.__destino = destino
        self.__avion = avion
        self.__billetes_comprados = []

    @property
    def origen(self):
        return self.__origen

    @origen.setter
    def origen(self, nuevo_origen):
        self.__origen = nuevo_origen

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, nuevo_destino):
        self.__destino = nuevo_destino

    @property
    def avion(self):
        return self.__avion

    @avion.setter
    def avion(self, nuevo_avion):
        self.__avion = nuevo_avion

    @property
    def billetes_comprados(self):
        return self.__billetes_comprados

    @billetes_comprados.setter
    def billetes_comprados(self, nuevo_billete):
        if len(self.__billetes_comprados) > self.__avion.capacidad:
            raise Exception('billetes_comprados', 'Se ha superado el límite de billetes posibles.')
        else:
            self.__billetes_comprados.append(nuevo_billete)