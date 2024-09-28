from abc import ABC, abstractmethod

# Definimos una interfaz usando una clase abstracta
class Calculos(ABC):
    
    @abstractmethod
    def _calcular_area(self):
        pass
    
    @abstractmethod
    def _calcular_perimetro(self):
        pass

    @abstractmethod
    def _imprimir(self):
        pass