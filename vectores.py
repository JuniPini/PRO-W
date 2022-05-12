vector1 = ['i','j','k']
vector2 = ['i','j','k']

resultado = ['i','j','k']

def imprimir_vector(vector):
    print("->", vector[0],'i, ', vector[1],'j, ',vector[2],'k')

def leer_vector(nombre_vector):
    vector  = ['i','j','k']

    letras = "ijk"    
    for letra in letras:
        vector[letras.index(letra)] = int(input("Introduce el elemento "+ letra +" del "+ nombre_vector +": "))


    return vector

vector1 = leer_vector("Vector 1")



vector2 = leer_vector("Vector 2")





resultado[0] = vector1[1] * vector2[2] - vector2[1] * vector1[2]
resultado[1] = vector1[0] * vector2[2] - vector2[0] * vector1[2]
resultado[2] = vector1[0] * vector2[1] - vector2[0] * vector1[1]


print("La multiplicación del vector 1: ")

imprimir_vector(vector1)


print("por el vector 2: ")

imprimir_vector(vector2)


print("Es igual a: ")

imprimir_vector(resultado)