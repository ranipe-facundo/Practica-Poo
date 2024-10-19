from abc import ABC, abstractmethod

class ConstructorDeTorta(ABC):
    
    @abstractmethod
    def agregar_masa(self,masa):
        pass
    
    @abstractmethod
    def agregar_relleno(self, relleno):
        pass