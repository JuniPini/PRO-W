class Persona:

    def __init__(self, nombre="", apellido1= '', apellido2='', edad=18, dni=""):
        #ponemos las variables en publico
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.dni = dni


    def mostrar(self):
        return "Nombre : " + self.__nombre + "\nEdad : " + str(self.__edad) + "\nDNI : " +str(self.__dni)
    
    def esMayorDeEdad(self):
        return self.__edad >= 18
           
    #añadimos los Getter
    @property
    def nombre(self):
        return self.__nombre
    #añadimos los Setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido1(self):
        return self.__apellido1

    @apellido1.setter
    def apellido1(self, nuevo_apellido1):
        self.__apellido1 = nuevo_apellido1

    @property
    def apellido2(self):
        return self.__apellido2

    @apellido2.setter
    def apellido2(self, nuevo_apellido2):
        self.__apellido2 = nuevo_apellido2
        
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int):
            self.__edad = nueva_edad
        else:
            print("El formato de la edad, no es valido")

    @property
    def dni(self):
        return self.__dni
    
    def validarNIF(self,nif):
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        restoLetra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

        if comprobacion[restoLetra] == letra: #buscar un elemento en una cadena mediante una posicion
            return True
        else: 
            return False
    
    @dni.setter
    def dni(self, nuevo_dni):
        if self.validarNIF(nuevo_dni):
            self.__dni = nuevo_dni
        else:
            print("El formato del dni no es valido")


'''class Persona:

    def __init__(self, nombre = '' , edad = 18, nif = ''):

        self.__edad = ''
        self.__nif = ''

        self.__nombre = nombre
        
        self.edad  = edad
        self.nif   = nif
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo



    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nuevo):
        if isinstance(nuevo, int) and nuevo < 120:
            self.__edad = nuevo
        else:
            print("[" + nuevo + "] No es formato de edad Inválido")


    def validarNIF(self,nif):
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        restoLetra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

        if comprobacion[restoLetra] == letra: #buscar un elemento en una cadena mediante una posicion
            return True
        else: 
            return False


    @property
    def nif(self):
        return self.__nif


    @nif.setter
    def nif(self,nuevo):
        if self.validarNIF(nuevo):
            self.__nif = nuevo
        else:
            print("["+ nuevo +"] No es un NIF válido")


    def mostrar(self):
        return "Persona: " + self.__nombre + " con edad: " + str(self.__edad) + " y NIF: " + self.__nif'''