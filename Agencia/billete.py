class Billete:

    def __init__(self):
        self.__viaje : str
        self.__nombre : str
        self.__apellidos : str

    @property
    def viaje(self):
        return self.__viaje

    @viaje.setter
    def viaje(self, nuevo_viaje):
        if not nuevo_viaje:
            raise Exception('viaje', 'No se han insertado viajes')
        else:
            self.__viaje = nuevo_viaje

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise Exception('nombre', 'No se han insertado nombres')
        else:
            self.__nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevos_apellidos):
        if not nuevos_apellidos:
            raise Exception("apellidos", "No se han insertado apellidos")
        else:
            self.__apellidos = nuevos_apellidos