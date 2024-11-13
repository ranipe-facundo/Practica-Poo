from abc import ABC, abstractmethod

class Personaje(ABC): #aca estoy diciendo que es una clase abstracta, eso 
    
    def __init__(self, vida, nivelAtaque, nivelDefensa, nombre):
        self._nombre = nombre
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa

    def atacar(self):
        return self._nivelAtaque
    
    @abstractmethod
    def defender(self):
        pass
    
    def ataca_a (self,atacado):
        atacado._vida = ( atacado._vida - (self.atacar() - atacado._nivelDefensa))