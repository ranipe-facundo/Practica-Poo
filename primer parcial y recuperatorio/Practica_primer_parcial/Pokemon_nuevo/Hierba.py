from Pokemon import Pokemon
import random

class Hierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Hierba", "Fuego")
    
    def defensa (self, ataque_enemigo):
        if self._defensa >= ataque_enemigo:
            pass
        if self._velocidad > 50 and random.randint(0, 100) > 50:
            pass
        self._vida = self._vida - (ataque_enemigo - self._defensa)
