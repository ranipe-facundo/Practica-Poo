from abc import ABC, abstractmethod

class Acciones_cuenta(ABC):
    
    @abstractmethod
    def agregar_saldo(self):
        pass
    
    @abstractmethod
    def pagar_debito(self):
        pass
    
    @abstractmethod
    def pagar_credito(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass