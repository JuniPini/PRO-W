from persona import Persona
import os

class Agenda(Persona):
    
    def __init__(self):
        self.anadir_persona = {}

    def fichero():
        f = open('/home/junior/Escritorio/personas.txt', 'w')
    def anadir_persona(self):

        nombre             = input("Introduce el Nombre del Contacto: ")
        primer_apellido    = input("Introduce el Primer Apellido del Contacto: ")
        segundo_apellido   = input("Introduce el Segundo Apellido del Contacto: ")
        nif                = input("Introduce el NIF del Contacto: ")
        edad               = int(input("Introduce la Edad del Contacto: "))
        direccion          = input("Introduce la Dirección del Contacto: ")
        email              = input("Introduce un E-mail para el Contacto: ")

    nueva_persona = Persona(nombre, primer_apellido,segundo_apellido, nif, edad, direccion, email)