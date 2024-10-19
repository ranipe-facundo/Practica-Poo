from AccionesPieza import AccionesPieza
from abc import ABC

class Pieza(AccionesPieza,ABC):
    def __init__(self, nombre, estado, color , ubicacion):
        self._nombre = nombre
        self._estado = estado
        self._color = color
        self._ubicacion = ubicacion
        
        def imprimir(self):
            print (self._color)
            print (self._estado)
            print (self._nombre)
            print (self._ubicacion)

        def posibles_movimientos(self):
            pass
        
        def mover(self):
            pass
        
        def comer(self):
            pass