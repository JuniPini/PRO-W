from Persona import Persona

class Contacto(Persona):

    """
    Un Contacto es una Persona que tiene además los siguientes campos:
        Dirección      -> direccion
        Teléfono Fijo  -> telefono_fijo
        Teléfono Móvil -> telefono_movil
        E-mail         -> email  
    """


    def __init__(self, nombre, primer_apellido,segundo_apellido, nif, edad, direccion, telefono_fijo, telefono_movil, email):
        super().__init__(nombre, primer_apellido,segundo_apellido, nif, edad)
        
        self.direccion = direccion

        #Con vaĺidación mediante variables privadas
        self.telefono_fijo  = telefono_fijo
        self.telefono_movil = telefono_movil
        self.email          = email


    @property
    def telefono_fijo(self):
        return self.__telefono_fijo

    @property
    def telefono_movil(self):
        return self.__telefono_movil

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if self.validar_email(nuevo_email):
            self.__email = nuevo_email


    def validar_email(self, email):
        return (email.count("@")==1) and ( email[-3:]==".es" or email[-4:]==".com") and (email.find(".es") > (email.find("@")+1) or  email.find(".com") > email.find("@")+1)

    @telefono_fijo.setter
    def telefono_fijo(self, nuevo_telefono):
        if self.validar_telefono(nuevo_telefono, False):
            self.__telefono_fijo = nuevo_telefono
        else:
            print("[Error] Ha insertado un teléfono fijo con formato no válido")
            exit

    @telefono_movil.setter
    def telefono_movil(self, nuevo_telefono):
        if self.validar_telefono(nuevo_telefono):
            self.__telefono_movil = nuevo_telefono
        else:
            print("[Error] Ha insertado un teléfono móvil con formato no válido")