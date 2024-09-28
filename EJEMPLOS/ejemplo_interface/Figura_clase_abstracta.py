from abc import ABC
#definimos una clase abstracta
class Figura(ABC):
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    
    