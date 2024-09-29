from abc import ABC
import random

class Pokemon(ABC):
    def __init__(self,nombre, tipo, debilidad):
        self._nombre = nombre
        self._tipo = tipo
        self._vida = random.randint(0,100)
        self._ataque = random.randint(0,100)
        self._defensa = random.randint(0,100)
        self._velocidad = random.randint(0,100)
        self._debilidad = debilidad
        self._salvajismo = random.randint(0,100)
        
    def get_debilidad(self):
        return self._debilidad
    
    def imprimir(self):
        print(f"Nombre: {self._nombre}")
        print(f"Ataque: {self._ataque}")
        print(f"Defensa: {self._defensa}")
        print(f"Velocidad: {self._velocidad}")
        print(f"Salvajismo: {self._salvajismo}")
        
    def ataque (self, pokemon_enemigo):
        if pokemon_enemigo.get_debilidad() == self._tipo:
            
            
    
    
# Ataque: Si el oponente tiene debilidad a este tipo (por ejemplo, un Pokémon de tipo Agua), hay
# un 70% de probabilidad de realizar un ataque crítico, lo que aumentará el ataque normal en un
# 50%. Para realizar este ataque se deberá recibir el pokémon al cual se atacará.
    
    
    
# Hierba        
# nombre, tipo, vida, ataque, defensa, velocidad, debilidad y salvajismo

# Fuego
# nombre, tipo, vida, ataque, defensa, velocidad, debilidad y salvajismo

# Agua
# nombre, tipo, vida, ataque, defensa, velocidad, debilidad y salvajismo