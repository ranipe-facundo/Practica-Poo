from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    def __init__(self,nombre, tipo, debilidad):
        self._nombre = nombre
        self._tipo = tipo
        self._vida = 100
        self._ataque = random.randint(0,100)
        self._defensa = random.randint(0,100)
        self._velocidad = random.randint(0,100)
        self._debilidad = debilidad
        self._salvajismo = random.randint(0,100)
        
    def get_debilidad(self):
        return self._debilidad
    def get_salvajismo(self):
        return self._salvajismo
    def get_vida(self):
        return self._vida
    
    def imprimir(self):
        print(f"Nombre: {self._nombre}")
        print(f"Ataque: {self._ataque}")
        print(f"Defensa: {self._defensa}")
        print(f"Velocidad: {self._velocidad}")
        print(f"Salvajismo: {self._salvajismo}")
        
    def ataque (self, pokemon_enemigo): #igual para Hierba y Fuego, redefinido en Agua
        if pokemon_enemigo.get_debilidad() == self._tipo and random.randint(0,100) <= 70:
            return self._ataque * 1.5
        else:
            return self._ataque
    
    @abstractmethod
    def defensa (self, ataque_enemigo): 
        pass
