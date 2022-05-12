from abc import abstractproperty


class Persona():
    
    def __init__(self, sexos = ["masculino", "femenino"], nombre = ""):
        
        self.sexos = sexos
        self.nombre = nombre

    @abstractproperty
    def sexos(self):
        return self.sexos

    @sexos.setter
    def sexos(self, nuevo_sexos):
        self.sexos = nuevo_sexos

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre