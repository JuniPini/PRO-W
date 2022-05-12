def ValidarNIF(nif):

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if not(nif[0:8].isnumeric()) or len(nif) != 9:
        return False
    else:
        if letras[int(nif[0:8])%23] != nif[8]:
            return False


    return True



nif = input("Introduzca un NIF válido: ")

if ValidarNIF(nif) : 
    print("El NIF es válido")
else:
    print("El NIF es inválido")




