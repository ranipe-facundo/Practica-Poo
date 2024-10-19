from abc import ABC, abstractmethod
import random

class Juego(ABC):
    def __init__(self, precio):
        self._id = random.randint(0,9999)
        self._precio = precio
    
    @abstractmethod
    def getPrecio(self):
        pass