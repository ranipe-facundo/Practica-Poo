from Carta import Carta
import random

class Oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self._velocidad = int(random.randint(74,90) * 1.05)
        self._tiro = int(random.randint(74,90) * 1.05)
        self._regate = int(random.randint(74,90) * 1.05)
        self._defensa = int(random.randint(74,90) * 1.05)
        self._pase = int(random.randint(74,90) * 1.05)
        self._fisico = int(random.randint(74,90) * 1.05)

#carta_oro = Oro("Emiliano Martinez", "Aston Villa", "Argentina")
#carta_oro.imprimir()