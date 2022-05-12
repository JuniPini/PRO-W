def insertar_en_lista(lista, cantidad_valores_a_insertar, texto_mensaje):

    numero = 0

    i = 0 

    while i < cantidad_valores_a_insertar:
        
        numero = input("["+ str(i+1) +"]" + texto_mensaje)
        
        if numero.isnumeric() and int(numero) > 0 and  int(numero) < 50  and int(numero) not in lista:       
            lista.append(int(numero))
            i += 1
        else:
            print("Error, el número", numero, "no es válido")
            

    return lista


lista_numeros = []
complento_reintegro = []


lista_numeros = insertar_en_lista(lista_numeros, 15, 'Inserte un número entre el 1 y el 49: ')

for i in range(len(lista_numeros)):
    for j in range(len(lista_numeros)):
        if lista_numeros[j] > lista_numeros[i]:
            aux = lista_numeros[i]
            lista_numeros[i] = lista_numeros[j]
            lista_numeros[j] = aux


complento_reintegro = insertar_en_lista(complento_reintegro, 1, 'Inserte un complementario: ')
complento_reintegro = insertar_en_lista(complento_reintegro, 1, 'Inserte el reintegro: ')


print(lista_numeros)
print(complento_reintegro)