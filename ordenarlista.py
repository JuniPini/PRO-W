lista_numeros=[]

numero="no"

while numero != "":
    numero= input("Introduce un número o pulse Enter para finalizar: ")

    if not numero in lista_numeros:
        lista_numeros.append(numero)

lista_numeros.sort

print(lista_numeros)


