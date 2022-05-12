
def emailValido(email):
    if (email.count("@")==1) and (email[-3:]==".es" or email[-4:]== ".com") and (email.find(".es") > (email.find("@")+1) or email.find(".com") > email.find("@")+1):
        return True
    else:
        return False


def nifValido(nif):
    
    if len(nif) == 9:
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        restoletra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

        if comprobacion[restoletra] == letra:
            return True
        else:
            return False

    return False

def telefonoValido(telefono):

    if len(telefono) == 9 and telefono.isnumeric():
        return True
    else:
        return False

opcion = ''

Usuarios = {}

while opcion != "T":
    opcion = input("Introduce una opción:\n[I] Insertar nuevo usuario\n[T] Terminar la ejecución del programa\n[M] Mostrar diccionario\n")

    opcion = opcion.upper()

    if opcion == "I":


        nif = input("Introduce un NIF válido: ")
        while not nifValido(nif):
            nif = input("Error, nif "+ nif + " inválido, introduce un NIF válido: ")

        usuario = {}

        nombre = input("Introduzca un nombre: ")
        apellidos = input("Introduzca un apellidos: ")
        direccion = input("Introduce tu dirección: ")
        edad = int(input("Introduzca un edad: "))
        sexo = input("Introduzca un sexo: ")

        usuario.setdefault('nombre', nombre)
        usuario.setdefault('apellidos', apellidos)
        usuario.setdefault('direccion', direccion)
        usuario.setdefault('edad', edad)
        usuario.setdefault('sexo', sexo)

        #Validar email
        email = '1'

        dic_emails = {}
        i = 0

        while email != '':


            email = input("["+ str(i) +"] Introduce un email válido: ")

            while not emailValido(email) and email != '':
                email = input("Error, el email "+ email + " es inválido. ["+ str(i) +"] Introduce un email válido: ")
            
            #email válido

            if emailValido(email):
                dic_emails.setdefault(i,email)
                i = i + 1

        usuario.setdefault('emails', dic_emails)

        #Validar telefono
        telefono = '1'
        dic_telefonos = {}
        i = 0

        while telefono != '':


            telefono = input("["+ str(i) +"] Introduce un telefono válido: ")

            while not telefonoValido(telefono) and telefono != '':
                telefono = input("Error, el telefono "+ telefono + " es inválido. ["+ str(i) +"] Introduce un telefono válido: ")
            
            #telefono válido

            if telefonoValido(telefono):
                dic_telefonos.setdefault(i,telefono)
                i = i + 1

        usuario.setdefault('telefonos', dic_telefonos)


        Usuarios.setdefault(nif,usuario)

    elif opcion == 'M':
        print(Usuarios)

print("Se ha finalizado el programa")

