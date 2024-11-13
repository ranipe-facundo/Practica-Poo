from abc import ABC

class Persona(ABC):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad