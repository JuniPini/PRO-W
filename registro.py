def emailValido(email):
    if (email.count("@")==1) and ( email[-3:]==".es" or email[-4:]==".com") and (email.find(".es") > (email.find("@")+1) or  email.find(".com") > email.find("@")+1):
        return True
    else:
        return False


def nifValido(nif):
    letra = nif[-1:].upper()
    dni = int(nif[0:8])
    restoLetra = dni % 23
    comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

    if comprobacion[restoLetra] == letra: #buscar un elemento en una cadena mediante una posicion
        return True
    else: 
        return False



opcion = ''
Usuarios = {}


while opcion != 'T':
    opcion = input("Inserte una de las siguientes opciones\n[I] Insertar usuario\n[B] Buscar algún dato\n[T] Terminar el programa\n")


    if opcion == 'I':

        nif = ''

        while not nifValido(nif):
            nif = input("Introduzca un NIF válido: ")

        nombre    = input("Introduce un nombre: ")
        apellidos = input("Introduce un apellido: ")
        direccion = input("Introduce una dirección: ")

        dic_emails = {}

        email = '1'
        i = 0
        while not emailValido(email) or email  != '':
            email = input("Introduzca un email válido: ")
            i = i + 1

            if emailValido(email):
                dic_emails.setdefault(i,email)

        dic_telefonos = {}

        telefono = 'x'
        i = 0
        while not telefono.isnumeric() or telefono != '':
            telefono = input("Introduzca un teléfono válido: ")
            i = i + 1
            if telefono.isnumeric():
                dic_telefonos.setdefault(i, telefono)
