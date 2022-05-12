from prueba2 import dosmilquince


def registrouser():

    usuarios={}
    print("Vamos a introducir un nuevo usuario: ")
    nif = input("Ingrese su NIF: ")
    while nif != "0":
        if nif: 
            nombre = input("Nombre de usuario: ")
            apellidos = input("Apellidos del usuario: ")
            direccion = input("Dirección del usuario: ")
            email = input("Introduce tu email: ")
            telefono = input("Introduce un teléfono: ")
            correcto = "X"
            while not correcto in ("SN"):
                print("{} - {} {}, {}, {}, {}"
                        .format(nif,nombre,apellidos,direccion,email,telefono))
                correcto = input("¿Son correctos estos datos? (S/N)").upper
            if correcto == "S":
                usuarios[nif]=[nombre,apellidos,direccion,email,telefono]
                print("El usuario {} {} ha sido añadido")
            else:
                print("El usuario no ha sido añadido")

        print("\n")
        print("Vamos a añadir a otro usuario, si no es el caso, ingrese 0.")
        dni = input("Ingrese NIF: ")
    return usuarios


def main():
    usuarios=registrouser()
    dosmilquince(usuarios)

if __name__== "__main__":
    main()