from abc import ABC, abstractmethod

class Componente(ABC):
    
    @abstractmethod
    def es_carpeta(self):
        pass