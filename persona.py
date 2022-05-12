import os


f = open('/home/junior/Escritorio/personas.txt', 'w')

class Persona():
    def __init__(self, nombre, apellido1, apellido2, email, dni, direccion, codigo_postal):
    
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.email = email
        self.dni = dni
        self.direccion = direccion
        self.codigo_p = codigo_postal

    def fichero():
        
        f.write(Persona('Junior', 'Pinillos', 'Santisteban', 'juniorpinillos123@gmil.com', '78819396Y', 'Arrecife', '35500'))

    @property
    def nombre(self):
        return self.__nombre

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if self.validaremail(nuevo_email):
            self.__email = nuevo_email

    def validar_email(self, email):
        return (email.count("@")==1) and ( email[-3:]==".es" or email[-4:]==".com") and (email.find(".es") > (email.find("@")+1) or  email.find(".com") > email.find("@")+1)

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

    @property
    def codigo_p(self):
        return self.codigo_p

    @codigo_p.setter
    def codigo_p(self, nuevo_codigo_postal):
        self.codigo_p = nuevo_codigo_postal

f.close()