from abc import ABC
from Acciones_cuenta import Acciones_cuenta
import random

class Cuenta(Acciones_cuenta, ABC):
    def __init__(self, duenio):
        self._duenio = duenio
        self._saldo = 0
        self._numero_cuenta = random.randint(0,999)
    
    def agregar_saldo(self, saldo):
        self._saldo = self._saldo + saldo
    
    def pago_debito(self, monto_a_debitar):
        if monto_a_debitar > self._saldo:
            print ("Saldo insuficiente.")
        self._saldo = self._saldo - monto_a_debitar
    
    def pagar_credito(self):
        pass
    
    def imprimir(self):
        print(f"Dueño cuenta: {self._duenio}")
        print(f"Numero cuenta: {self._numero_cuenta}")
        print(f"saldo cuenta: {self._saldo}")