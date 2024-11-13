from abc import ABC, abstractmethod
import random

class Cuenta(ABC):
    def __init__(self, duenio):
        self._duenio = duenio
        self._saldo = 0
        self._numero_cuenta = random.randint(0,999)

    def imprimir(self):
        print(f"Dueño cuenta: {self._duenio}")
        print(f"Numero cuenta: {self._numero_cuenta}")
        print(f"saldo cuenta: {self._saldo}")
    
    def ingresar_saldo(self, saldo):
        self._saldo = self._saldo + saldo

    def pago_debito(self, monto_a_debitar):
        if monto_a_debitar > self._saldo:
            print ("Saldo insuficiente.")
        self._saldo = self._saldo - monto_a_debitar
        
    @abstractmethod
    def pagar_credito (self, monto_a_pagar, cantidad_cuotas):
        pass