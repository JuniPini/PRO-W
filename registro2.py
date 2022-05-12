###############################################
#      Función para validar E-mail            #
###############################################
def emailValido(email):
   if (email.count("@")==1) and ( email[-3:]==".es" or email[-4:]==".com") and (email.find(".es") > (email.find("@")+1) or  email.find(".com") > email.find("@")+1):
       return True
   else:
       return False
 
##########################################
#      Función para validar NIF          #
##########################################
def nifValido(nif):
 
   if len(nif) == 9 :
       letra = nif[-1:].upper()
       dni = int(nif[0:8])
       restoLetra = dni % 23
       comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
 
       if comprobacion[restoLetra] == letra: #buscar un elemento en una cadena mediante una posicion
           return True
       else:
           return False
 
   return False

###############################################
#      Función para validar Teléfono          #
###############################################
def telefono_valido(telefono):

    if len(telefono)== 9 and telefono.isnumeric():
        return True
    else:
        return False


#inicializamos a vacío para no repetir la pregunta.
opcion = ''

Usuarios = {}

while opcion != 'T':
    
    
    #Menú de selección
    opcion = input("Introduce una opción:\n[I] Insertar nuevo usuario\n[B] Buscar una palabra\n[T] Terminar la ejecución del programa\n[M] Mostrar diccionario\n")

    opcion = opcion.upper()

    # Insertar nuevo usuario
    if opcion == 'I':




        nif = input ("Introduce un NIF válido: ")
        while not nifValido(nif):
            nif = input ("Error, nif "+ nif +" inválido, introduce un NIF válido: ")


        usuario = {}

        nombre = input("Introduzca un nombre válido: ")
        apellidos = input("Introduzca apellidos válidos: ")
        direccion = input("Introduzca la dirección de "+ nombre + " "+ apellidos +": ")

        usuario.setdefault('nombre', nombre)
        usuario.setdefault('apellidos', apellidos)
        usuario.setdefault('direccion', direccion)


        ################################################
        #           Válidación de emails               #
        ################################################
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

        ###################################################
        #           Válidación de teléfonos               #
        ###################################################

        telefono = '1'

        dic_telefonos = {}
        i = 0

        while telefono != '':


            telefono = input("["+ str(i) +"] Introduce un telefono válido: ")

            while not telefono_valido(telefono) and telefono != '':
                telefono = input("Error, el telefono "+ telefono + " es inválido. ["+ str(i) +"] Introduce un telefono válido: ")
            
            #telefono válido

            if telefono_valido(telefono):
                dic_telefonos.setdefault(i,telefono)
                i = i + 1

        usuario.setdefault('telefonos', dic_telefonos)


        Usuarios.setdefault(nif,usuario)



    # Buscar palabra clave en el diccionario
    elif opcion == 'B':


        UsuariosEncontrados = {}


        palabra_a_buscar = input("Introduzca una palabra a buscar: ")
        
        #Recorremos los 3 niveles de nuestra estructura de diccionarios
        for nif, dic_usuario in Usuarios.items(): # Primer nivel de claves nif y valores de diccionarios de usuarios
            if palabra_a_buscar.lower() in nif.lower():
                UsuariosEncontrados.setdefault(nif, dic_usuario)
            for dato_usuario, valor_dato_usuario in dic_usuario.items(): # Primer nivel de claves datos y valores de datos y diccionarios de email, telefonos

                if dato_usuario != 'emails' and dato_usuario != 'telefonos':
                    if palabra_a_buscar.lower() in valor_dato_usuario.lower():
                        UsuariosEncontrados.setdefault(nif, dic_usuario)
                else:
                    for i, email_o_telefono in valor_dato_usuario.items(): # Tercer nivel solo cuando los valores del anterior nivel son diccionarios
                        if palabra_a_buscar.lower() in email_o_telefono.lower():
                            UsuariosEncontrados.setdefault(nif, dic_usuario)


        print(UsuariosEncontrados)

    # Mostrar el diccionario
    elif opcion == 'M':
        print(Usuarios)

print("Se ha finalizado el programa")