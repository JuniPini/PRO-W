class Coleccion():
    def estaVacia(self):
        pass

    def extraer(self):
        pass

    def primero(self):
        pass

    def añadir(self):
        pass

    def ultimo(self):
        pass


class Pila(Coleccion):
    
    def __init__(self):
        self.Coleccion = []
    
    def estaVacia(self):#devuelve true si la colección está vacía y false en caso contrario.
        if self.Coleccion:
            return True
        else:
            return False
    
    def extraer(self): #devuelve y elimina el primer elemento de la colección.
        print(self.Coleccion[1])
        self.Coleccion.remove(1)
        
    
    def primero(self): #devuelve el primer elemento de la colección.
        print(self.Coleccion[1])
        
    
    def añadir(self): #añade un elemento por el extremo que corresponda, y devuelve true si se ha añadido y false en caso contrario.
        if self.Coleccion.append(input("Introduce el elemento: ")):
            return True
        else:
            return False
        
    
    def ultimo(self): #devuelve el último elemento de la colección.
        print(self.Coleccion[-1])
        

class Cola(Coleccion):
    
    def __init__(self):
        self.Coleccion = []

    def estaVacia(self):
        if self.Coleccion:
            return True 
        else:
            return False
    
    def extraer(self):
        print(self.Coleccion[1])
        self.Coleccion.remove(1)

    def primero(self):
        print(self.Coleccion[1])

    def añadir(self):
        if self.Coleccion.append(input("Introudce el elemento: ")):
            return True
        else:
            return False

    def ultimo(self):
        print(self.Coleccion[-1])