dominios=["com", "es"]

def ValidarEmail(email):
    if not len(email.found("@")):
        



email=input("Introduce un correo válido: ")
if ValidarEmail(email):
    print("El email es válido")
else:
    print("El email es inválido")