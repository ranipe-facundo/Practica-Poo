from abc import ABC,abstractmethod

class Transporte(ABC):

    @abstractmethod
    def tansportarPaquete(self):
        pass
    
    @abstractmethod
    def calcularTiempo(self):
        pass
    
    