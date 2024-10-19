from Carta import Carta
import random
from listas import Lista_habilidades_especiales 

class Bronce_especial(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self.__habilidad_especial = self.__dar_habilidad_especial()
        self._velocidad = int(random.randint(49,65) +2)
        self._tiro = int(random.randint(49,65) +2)
        self._regate = int(random.randint(49,65) +2)
        self._defensa = int(random.randint(49,65) +2)
        self._pase = int(random.randint(49,65) +2)
        self._fisico = int(random.randint(49,65) +2)
        
    def __dar_habilidad_especial(self):
        return random.choice(Lista_habilidades_especiales)
    
    def imprimir(self):
        print("Habilidad Especial")
        print(self.__habilidad_especial)
        return super().imprimir()

#bronce = Bronce_especial("messi", "inter miami", "Argentina")
#bronce.imprimir()