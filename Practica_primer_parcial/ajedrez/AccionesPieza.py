from abc import ABC, abstractmethod

class AccionesPieza(ABC):

        @abstractmethod
        def posibles_movimientos(self):
            pass
        
        @abstractmethod
        def mover(self):
            pass
        
        @abstractmethod
        def comer(self):
            pass
        
        @abstractmethod
        def imprimir(self):
            pass
