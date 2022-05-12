'''n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")'''
# class Coleccion:

#     def estaVacia(self):
#         pass

#     def extraer(self):
#         pass

#     def primero(self):
#         pass

#     def anadir(self):
#         pass

#     def ultimo(self):
#         pass

# class LIFO(Coleccion):

#     def __init__(self):

#         self.lifo = []
    
#     def estaVacia(self):
#         return self.lifo == []
    
#     def extraer(self):
        
#         elemento = self.lifo[-1]

#         self.lifo.pop()

#         return elemento
    
#     def primero(self):

#         return self.lifo[:1]
    
#     def anadir(self, nuevo):

#         self.lifo.append(nuevo)

#         if nuevo == self.lifo[-1]:
#             return True
#         else:
#             return False

#     def ultimo(self):
        
#         return self.lifo[-1]

#     def __str__(self):
#         return str(self.lifo)

# class FIFO(Coleccion):
    
#     def __init__(self):
#         self.fifo = []


#Falta terminar el constructor de arriba
# cadena = 'hola' 

# def AllUpper():
#     if cadena == cadena.upper():
#         return True 
#     else: 
#         return False
import tkinter as tk

window = tk.Tk()