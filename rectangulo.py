class Rectangulo():
    def __init__(self, inicio= 0, final = 0):
        
        self.inicio = inicio
        self.final = final

    @property
    def inicio(self):
        return self.inicio

    @property
    def final(self):
        return self.final