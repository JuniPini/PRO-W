
cesta = {}

producto = 0

while producto != "":

    producto = input("Introduzca un producto en la cesta de la compra: ")


    if producto != '':
        precio = ''
        while not precio.replace('.','').isnumeric():
            precio = input("Introduzca el precio de "+ producto + ": ")

        cesta.setdefault(producto,float(precio))


precio_total = 0.0
for producto, precio in cesta.items():
    print(producto,precio)

    precio_total = precio_total + precio

print("El precio total de la cesta es: ", precio_total)