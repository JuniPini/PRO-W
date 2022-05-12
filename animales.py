lista_animales=["Perro", "Gato", "Elefante", "Girafa"]

animal= "no"


while animal != "" :
    animal= input("Inserte un animal en la lista o pulse Enter para finalizar: ")

    if animal !="" :
        animal= animal[0].upper() + animal[1:].lower()

    if not animal in lista_animales:
        lista_animales.append(animal)

lista_animales.pop()

lista_animales.remove("Perro")

lista_animales.remove("Gato")

print(lista_animales)
