'''Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y valor será otro diccionario formado por pares de clave/valor del tipo modulo/nota (entero).

Al final el programa nos mostrará el diccionario de alumnos y la nota media obtenida por cada uno de ellos. 

Obtener:
{
    'Juan Fransisco : {
        'Programación' : 6
       ,'Redes' : 4
    }
    ,'Andrés': {
        'Lenguaje de marcas' : 7
       ,'Matemáticas' : 3
    }

}


Resultado:
{
    'Juan Fransisco : 5
    ,'Andrés': 5
}'''

Alumnos = {}
#Registrar alumnos

alumno = {}

nombre = input("Introduce el nombre del alumno: ")
apellidos = input("Introduce los apellidos del alumno: ")

alumno.setdefault('nombre', nombre)
alumno.setdefault('apellidos', apellidos)

#Introducir módulos
modulo = "1"

dic_modulo = {}

i = 0

while modulo != "":
    modulo = input("["+ str(i)+"] Introduce el nombre del módulo: ")
    dic_modulo.setdefault(i, modulo)
    i = i + 1

alumno.setdefault('Módulo', dic_modulo)
#Introducir notas

notas = "1"

dic_notas = {}

while notas != "":
    notas = input("["+ str(i)+"] Introduce la nota del módulo: ")
    dic_notas.setdefault(i, notas)
    i = i + 1

alumno.setdefault('Nota', dic_notas)

Alumnos.setdefault(nombre, alumno)

print(Alumnos)

'''modulo = {}

i = 0

while nombre_modulo != '':
    nombre_modulo = input("Introduce los módulos que tienes: ")
    modulo.setdefault(i, nombre_modulo)
    i = i + 1 

alumno.setdefault("Módulo", modulo)

notas = {}

i = 0

while notas_modulo != '':
    notas_modulo = int(input("Introduce nota: "))
    notas.setdefault(i, notas_modulo)
    i = i + 1

alumno.setdefault('nota', notas)

alumnos.setdefault(nombre, alumno)

print(alumnos)'''