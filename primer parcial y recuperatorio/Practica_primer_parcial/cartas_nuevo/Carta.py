from abc import ABC, abstractmethod

class Carta(ABC):
    def __init__(self, nombre, club, pais):
        self._nombre = nombre
        self._club = club
        self._pais = pais
        self._velocidad = 0
        self._tiro = 0
        self._regate = 0 
        self._defensa = 0
        self._pase = 0
        self._fisico = 0
        
    def get_pais(self):
        return self._pais
    def get_club(self):
        return self._club

    def imprimir(self):
        print(self._nombre)
        print (self._club)
        print (self._pais)
        print (f"Valoracion {int((self._velocidad + self._tiro + self._regate + self._defensa + self._pase + self._fisico) / 6 )}")
        print (f"Velocidad: {self._velocidad} Tiro: {self._tiro}")
        print (f"Regate: {self._regate} Defensa: {self._defensa}")
        print (f"Pase: {self._pase} Fisico: {self._fisico}")

#nombre, club, país, velocidad, tiro, regate, defensa, (leo es loco)
#pase y físico.          habilidad especial

#nombre, equipo, país y una
#habilidad especial.
#============================================================================

#: nombre, club, país, velocidad, tiro, regate, defensa,
#pase y físico

# nombre, equipo y país.
#======================================================================

#club, país, especiales, velocidad, tiro, regate, defensa, 
#pase y físico.    una lista de habilidades

# nombre, equipo, país