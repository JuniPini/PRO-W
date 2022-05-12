class DispositivoElectronico():

    def __init__(self, nombre, marca, precio):
        
        #Aquí guardaremos los datos necesarios para la clase.

        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def marca(self):
        return self.marca

    @marca.setter
    def marca(self, nueva_marca):
        self.marca = nueva_marca

    @property
    def precio(self):
        return self.precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.precio = nuevo_precio
        if nuevo_precio.isnumeric():
            return nuevo_precio
            
    def __str__(self):

        return "El nombre del dispostivo es " + str(self.nombre) + ", la marca es " + str(self.marca) + "y el precio de este es " + str(self.precio) + "€."

class Compania():
    compania = {
        "OR":"Orange",
        "MS":"Movistar",
        "VF":"Vodafone",
        "MM":"Más Movil"
    }

class Telefono(DispositivoElectronico, Compania):
    
    def __init__(self, nombre, marca, precio, numero, compania):
        super().__init__(nombre, marca, precio)

        #Introduciremos los nuevos datos de la nueva clase

        self.numero = numero
        self.compania = compania

    @property
    def numero(self):
        return self.numero

    @numero.setter
    def numero(self, nuevo_numero):
        self.numero = nuevo_numero
        if nuevo_numero.isnumeric() and range(nuevo_numero) < 9 and range(nuevo_numero) > 1:
            return nuevo_numero

    @property
    def compania(self):
        return self.compania
    
    def validarCompania(self, nueva_compania):
        self.compania = nueva_compania
        if nueva_compania == Compania:
            return nueva_compania


class Portatil(DispositivoElectronico):
    
    def __init__(self, nombre, marca, precio, resolucion, tamanio):
        super().__init__(nombre, marca, precio)

        #Introcimos los nuevos valores de la clase.
        self.resolucion = resolucion
        self.tamanio = tamanio

    @property
    def resolucion(self):
        return self.resolucion

    @resolucion.setter
    def resolucion(self, nueva_resolucion):
        self.resolucion = nueva_resolucion

    @property
    def tamanio(self):
        return self.tamanio

    @tamanio.setter
    def tamanio(self, nuevo_tamanio):
        self.tamanio = nuevo_tamanio
        if nuevo_tamanio.isnumeric() and range(nuevo_tamanio) > 6 and range(nuevo_tamanio) < 140:
            return nuevo_tamanio

movil = DispositivoElectronico("S20", "Samsung", 500)

print(movil)
        