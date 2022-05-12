from alojamiento import Alojamiento

class Hotel(Alojamiento):
    def __init__(self, direccion, provincia, pais, gerente, estrellas, director, piscina):
        super().__init__(direccion, provincia, pais, gerente)
        
        self.estrellas = estrellas
        self.director = director
        self.piscina = piscina

    @property
    def estrellas(self):
        return self.__estrellas

    @estrellas.setter
    def estrellas(self, nuevas_estrellas):
        if isinstance(nuevas_estrellas, int) and nuevas_estrellas >= 1 and nuevas_estrellas <= 5:
            self.estrellas = nuevas_estrellas
        else:
            print("[ERROR] El número introducido no corresponde a las estrellas en un hotel")
            exit

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, nuevo_director):
        if len(nuevo_director) > 5:
            self.__director = nuevo_director
        else:
            print("[ERROR] EL nombre de director es demasiado corto")

    @property
    def piscina(self):
        return self.__piscina

    @piscina.setter
    def piscina(self, nueva_piscina):
        self.__piscina = bool(nueva_piscina)