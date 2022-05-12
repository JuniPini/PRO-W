palabra = input("Introduce un palíndromo: ")

if palabra == palabra [::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


'''palabra=input("inserte una palabra :")

pos = len(palabra)

palabra_reverse = ''

for letra in palabra:
    palabra_reverse = palabra_reverse + palabra[pos-1]
    pos -= 1


if palabra_reverse == palabra:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")'''