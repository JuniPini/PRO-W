from pais import Pais
from provincia import Provincia

class Alojamiento:
    """
    Dirección: (Dónde se encuentra el alojamiento)
    Provincia: (abreviado en 2 números, los dos primeros dígitos del código postal)
    País: (abreviado en 2 siglas)
    Gerente
    """

    def __init__(self, direccion, provincia, pais, gerente):

        self.direccion = direccion
        self.provincia = provincia
        self.pais      = pais
        self.gerente   = gerente
        

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self,nueva_direccion):

        if len(nueva_direccion) > 5 : 
            self._direccion = nueva_direccion
        else:
            print("[Error] La dirección es demasiado corta")
            exit



    @property
    def provincia(self):
        return self._provincia


    @provincia.setter
    def provincia(self,nueva_provincia):

        if nueva_provincia in Provincia.codigo: 
            self._provincia = nueva_provincia
        else:
            print("[Error] La provincia insertada no existe")
            exit


    @property
    def pais(self):
        return self._pais


    @pais.setter
    def pais(self,nueva_pais):

        if nueva_pais in Pais.codigo: 
            self._pais = nueva_pais