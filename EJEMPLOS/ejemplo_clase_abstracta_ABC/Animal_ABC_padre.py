from abc import ABC, abstractmethod

# Clase abstracta Animal
class Animal(ABC):
    
    def __init__(self, nombre, edad, color):
        self._nombre = nombre
        self._edad = edad
        self._color = color

    # Método abstracto que debe implementarse en las subclases
    @abstractmethod
    def hacer_sonido(self):
        pass

    # Método común para las subclases
    def comer(self):
        print(f"{self._nombre} está comiendo.")

    # Otro método común para las subclases
    def dormir(self):
        print(f"{self._nombre} está durmiendo.")