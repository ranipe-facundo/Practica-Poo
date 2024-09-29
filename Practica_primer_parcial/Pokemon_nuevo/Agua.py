from Pokemon import Pokemon
import random

class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Agua", "Hierba")
    
    def ataque (self, pokemon_enemigo): #igual para Hierba y Fuego, redefinido en Agua
        if pokemon_enemigo.get_debilidad() == self._tipo:
            return self._ataque * 1.7
        else:
            return self._ataque
    
    def defensa (self, ataque_enemigo):
        if self._defensa >= ataque_enemigo:
            pass
        if random.randint(0,100) <= 30:
            self._vida = self._vida - (self._defensa - int(ataque_enemigo/2))
        else:
            self._vida = self._vida - (self._defensa - ataque_enemigo)