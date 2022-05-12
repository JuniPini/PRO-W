# from tkinter import Y
# from typing_extensions import Self


# class Vector():
#     def __init__(self, x, y, k):
#         self.__x = x
#         self.__y = y
#         self.__k = k

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, nueva_x):
#         self.__x = nueva_x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, nueva_y):
#         self.__y = nueva_y

#     @property
#     def k(self):
#         return self.__k

#     @k.setter
#     def k(self, nueva_k):
#         self.__k = nueva_k

class Vector:
    def __init__(self, i = 0, j = 0, k = 0):

        self.__i = i
        self.__j = j
        self.__k = k

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j

    @property
    def k(self):
        return self.__k        


    def __str__(self):

        return "("+ str(self.__i) +"i,"+ str(self.__j) +"j,"+ str(self.__k) +"k)"


    # **
    def __pow__(self, aux):

        return self.__i * aux.i + self.__j + aux.j + self.__k + aux.k


    # *
    def __mul__(self, aux):


        i =  self.__j * aux.k - aux.j * self.__k

        j = - self.__i * aux.k - aux.i * self.__k

        k = + self.__i * aux.j - aux.i * self.__j



        return Vector(i,j,k)


u = Vector(3,1,0)
v = Vector(2,1,-1)

#producto escalar
y = u ** v


#producto vectorial
z = u * v



print("El producto escalar de u ** v es igual a: " + str(y))
print("El producto vectorial de u * v es igual a: ", z)