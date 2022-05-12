class Empleado():

    def __init__(self, nombre, apellidos, direccion, codigopostal, salario):

        #Añadimos la información con la que vamos a trabajar.
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.codigopostal = codigopostal
        self.salario = salario

    
    #Añadimos los getters y los setters.
    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.apellidos

    @apellidos.setter
    def apellidos(self, nuevo_apellidos):
        self.apellidos = nuevo_apellidos
    
    @property
    def direccion(self):
        return self.direccion

    @direccion.setter
    def direccion(self, nuevo_direccion):
        self.direccion = nuevo_direccion

    @property
    def codigopostal(self):
        return self.codigopostal

    @codigopostal.setter
    def codigopostal(self, nuevo_codigopostal):
        self.codigopostal = nuevo_codigopostal
        if not nuevo_codigopostal.isnumeric() and not len(nuevo_codigopostal) <= 5:
            return print("No es un código postal válido.")

    @property
    def salario(self):
        return self.salario

    @salario.setter
    def salario(self, nuevo_salario):
        self.salario = nuevo_salario
        if nuevo_salario >= 1000 or nuevo_salario <= 1200:
            return print("El salario no es correcto")


class Cocinero(Empleado):

    def __init__(self, nombre, apellidos, direccion, codigopostal, salario, plato_elaborado):
        super().__init__(nombre, apellidos, direccion, codigopostal, salario)

        self.plato_elaborado = plato_elaborado
        


    @property
    def plato_elaborado(self):
        return self.plato_elaborado

    @plato_elaborado.setter
    def plato_elaborado(self, nuevo_plato_elaborado):
        self.plato_elaborado = nuevo_plato_elaborado

    @property
    def salario(self):
        return super().salario

    @salario.setter
    def salario(self, nuevo_salario):
        self.salario = nuevo_salario
        if nuevo_salario >= 1500 or nuevo_salario <= 2500:
            return print("El salario no es correcto")