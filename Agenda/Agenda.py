from Contacto import Contacto


class Agenda:

    def __init__(self):
        self.agenda = {}


    def anadir_contacto(self):

        nombre             = input("Introduce el Nombre del Contacto: ")
        primer_apellido    = input("Introduce el Primer Apellido del Contacto: ")
        segundo_apellido   = input("Introduce el Segundo Apellido del Contacto: ")
        nif                = input("Introduce el NIF del Contacto: ")
        edad               = int(input("Introduce la Edad del Contacto: "))
        direccion          = input("Introduce la Dirección del Contacto: ")
        telefono_fijo      = int(input("Introduce un Teléfono Fijo para el Contacto: "))
        telefono_movil     = int(input("Introduce un Teléfono Móvil para el Contacto: "))
        email              = input("Introduce un E-mail para el Contacto: ")


        

        while nombre in self.agenda:

            print("El contacto, ya existe en la agenda")
            nombre = input("Introduce el Nombre del Contacto: ")


        nuevo_contacto = Contacto(nombre, primer_apellido,segundo_apellido, nif, edad, direccion, telefono_fijo, telefono_movil, email)


        self.agenda[nombre] = nuevo_contacto
        #self.agenda = {nombre : nuevo_contacto}

    def listar_contactos(self):
        print(self.agenda.sort())


    def buscar_contactos(self):


        campo_a_buscar = input("Introduzca el valor del campo a buscar: ")

        encontrados = {}

        for nombre, contacto in self.agenda.items():

            if campo_a_buscar in nombre:
                encontrados[nombre] = contacto
            elif campo_a_buscar in contacto.primer_apellido:
                encontrados[nombre] = contacto               
            elif campo_a_buscar in contacto.nif:
                encontrados[nombre] = contacto
            elif campo_a_buscar in contacto.email:
                encontrados[nombre] = contacto
            
        return encontrados

    def editar_contactos(self):

        campo_a_modificar = input("Introduzca el valor del campo a modificar: ")

        encontrados = {}

        for nombre, Contacto in self.agenda.items():
            if campo_a_modificar in nombre:
                encontrados[nombre] = 