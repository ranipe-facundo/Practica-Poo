from abc import ABC, abstractmethod
import random

class Cuenta(ABC):
    
    def __init__(self, dueno):
        self._dueno = dueno
        self._saldo = 0
        self._nro_cuenta = random.randint(100,9999)

    @abstractmethod
    def pagar_debito(self):
        pass
    @abstractmethod
    def pagar_credito(self):
        pass
