class Persona:
    """
        Gestiona las personas, como seres humanos:
        Nombre              -> nombre
        Primer apellido     -> primer_apellido
        Segundo apellido    -> segundo_apellido
        NIF                 -> nif
        Edad                -> edad
    """

    def __init__(self, nombre, primer_apellido,segundo_apellido, nif, edad):
        self.nombre           = nombre
        self.primer_apellido  = primer_apellido
        self.segundo_apellido = segundo_apellido

        self.nif  = nif 
        self.edad = edad

    @property
    def nif(self):
        return ""

    @property
    def edad(self):
        return ""

    @nif.setter
    def nif(self, nuevo_nif):
        if self.validar_nif(nuevo_nif):
            self._nif = nuevo_nif
        else:
            print("[Error] el NIF: ", nuevo_nif, "no tiene un formato válido")
            exit

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0 and nueva_edad <= 130:
            self._edad = nueva_edad
        else:
            print("[Error] la edad: ", nueva_edad, "no tiene un formato válido")
            exit

    def validar_nif(self, nif):
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        restoLetra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

        return comprobacion[restoLetra] == letra


    def mostrar(self):
        return "Nombre: "+ self.nombre + " Primer Apellido: " + self.primer_apellido + " Segundo Apellido: " + self.segundo_apellido + " NIF: " + self._nif +" Edad: "+ str(self._edad)

