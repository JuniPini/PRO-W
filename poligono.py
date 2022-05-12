
from abc import ABC, abstractmethod


class Poligono(ABC):
    @abstractmethod
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.base
    
    @base.setter
    def base(self, nuevo_base):
        self.base = nuevo_base

    @property
    def altura(self):
        return self.altura

    @altura.setter
    def altura(self, nueva_altura):
        self.altura = nueva_altura

    