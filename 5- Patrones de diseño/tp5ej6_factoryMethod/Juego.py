from abc import ABC, abstractmethod
import random

class Juego(ABC):
    def __init__(self, precio):
        self._id = random.randint(0,9999)
        self._precio = precio
        self._precio_final = 0
        
    @abstractmethod
    def getPrecio(self):
        pass 
    
    def imprimir(self): #esto no lo pide el ejercicio
        print(f'ID Juego: {self._id}')
        print (f'Precio base: ${self._precio}')