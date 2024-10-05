from abc import ABC, abstractmethod

class Acciones_cuenta(ABC):
    
    def agregar_saldo(self):
        pass
    
    def pagar_debito(self):
        pass
    
    def pagar_credito(self):
        pass
    
    def imprimir(self):
        pass
