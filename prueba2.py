def alumnosdic():
 
    dicc = {}
    print("Vamos a cargar los datos del alumno:")
    dni=input("Ingrese DNI: ")
    while dni!= "0":
        # Tomamos datos sólo si DNI no es nulo (retorno de carro sin texto)
        if dni:
            alumno=input("Nombre del alumno: ")
            apellido=input("Apellido del alumno: ")
            anodecursada=input("Año de cursada: ")
            # Bucle para cerciorarnos que ha introducido SI o NO. Forzamos a mayúsculas.
            aprobado = "X"
            while not aprobado in ("SN"):
                aprobado=input("Ingrese condicion de aprobado (S/N): ").upper()
 
            # Bucle para cerciorarnos que ha introducido SI o NO. Forzamos a mayúsculas.
            correcto = "X"
            while not correcto in ("SN"):
                print("{} - {} {}, Año: {} => {}"
                      .format(dni,alumno,apellido,anodecursada,{"S":"APROBADO","N":"SUSPENSO"}[aprobado]))
                correcto=input("¿Son correctos estos datos? (S/N)").upper()
            if correcto == "S":
                dicc[dni]=[alumno,apellido,anodecursada,aprobado]
                print("La carga del alumno {} {} ha finalizado.".format(alumno,apellido))
            else:
                print("La carga del alumno actual ha sido anulada...")
 
        print("\n")
        print("Vamos a cargar los datos del siguiente alumno, en el caso de que ya halla finalizado de cargarlos a todos, ingrese 0.")
        dni = input("Ingrese DNI: ")
    return dicc
 
 
 
 
 
def dosmilquince(dicc):
    for valor in dicc:
        # Asignamos variables para mayor calidad visual. No repercute ni en memoria ni en velocidad de procesamiento.
        dni = valor
        alumno       = dicc[dni][0]
        apellido     = dicc[dni][1]
        anodecursada = dicc[dni][2]
        aprobado     = dicc[dni][3]
        if anodecursada=="2015" and aprobado=="S":
            print("{} - {} {}, Año: {} => {}"
                      .format(dni,alumno,apellido,anodecursada,{"S":"APROBADO","N":"SUSPENSO"}[aprobado]))
 
 
def main():
    dicc=alumnosdic()
    dosmilquince(dicc)
 
if __name__ == "__main__":
    main()