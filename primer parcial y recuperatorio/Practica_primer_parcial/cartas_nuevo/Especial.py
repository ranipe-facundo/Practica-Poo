from Carta import Carta
import random
from listas import Lista_habilidades_especiales

class Especial(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self._velocidad = self.__calcular_caracteristicas()
        self._tiro = self.__calcular_caracteristicas()
        self._regate = self.__calcular_caracteristicas()
        self._defensa = self.__calcular_caracteristicas()
        self._pase = self.__calcular_caracteristicas()
        self._fisico = self.__calcular_caracteristicas()
        self.__habilidades_especiales = self.__dar_habilidades()
    
    def __calcular_caracteristicas(self):
        numero = random.randint(74,90) * 1.05
        if numero > 99:
            return 99
        else:
            return int(numero)
    
    def __dar_habilidades(self):
        lista = []
        for i in range (3):
            lista.append(random.choice(Lista_habilidades_especiales))
        return lista

    def imprimir(self):
        print("Habilidad")
        for i in self.__habilidades_especiales:
            print(i)
        return super().imprimir()

#carta_especial = Especial("Julian Alvarez", "Atletico Madrid", "Argentina")
#carta_especial.imprimir()