
from alojamiento import Alojamiento
from elementos_cocina import ElementosCocina


class Apartamento(Alojamiento):

    def __init__(self, direccion, provincia, pais, gerente,llaves, elementos_cocina):
        super().__init__(direccion, provincia, pais, gerente)

        self.llaves = llaves
        self.__elementos_cocina = []
        self.elementos_cocina = elementos_cocina



    @property
    def llaves(self):
        return self.__llaves

    @llaves.setter
    def llaves(self,nuevo_valor):

        if isinstance(nuevo_valor, int) and nuevo_valor >= 1 and nuevo_valor <= 4:
            self.__llaves = nuevo_valor
        else:
            print("[Error] El formato de las llaves no es válido.")
            exit

    @property
    def elementos_cocina(self):
        return self.__elementos_cocina

    @elementos_cocina.setter
    def elementos_cocina(self,nuevo_valor):

        if nuevo_valor in ElementosCocina.codigo:
            
            if nuevo_valor not in self.__elementos_cocina:
                self.__elementos_cocina.append(nuevo_valor)
            else:
                print("[Error] el ya ha sido insertado")
                exit
        else:
            print("[Error] el elemento no existe")
            exit


    def __str__(self):

        #objeto = " ".join(self.__elementos_cocina)

        elemento_cocina_cadena = ''
        for elemento_cocina in self.__elementos_cocina:
            elemento_cocina_cadena = elemento_cocina_cadena + ElementosCocina.codigo[elemento_cocina]

        return super().mostrar() + "; Llaves: " + str(self.__llaves) + "; Elementos Cocina: " + elemento_cocina_cadena