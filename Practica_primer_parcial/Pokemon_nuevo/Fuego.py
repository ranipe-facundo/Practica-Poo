from Pokemon import Pokemon

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Fuego", "Agua")
    
    def defensa(self, ataque_enemigo):
        if self._defensa >= ataque_enemigo:
            pass
        else:
            self._vida = self._vida - (ataque_enemigo - self._defensa)
