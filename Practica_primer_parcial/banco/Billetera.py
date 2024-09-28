from Cuenta import Cuenta
import random

class Billetera(Cuenta):
    def __init__(self, dueno):
        super().__init__(dueno)
        self.__cvu = random.randint(100,9999)
    
    def pagar_debito(self,monto):
        self._saldo = self._saldo - monto
    
    def pagar_credito(self,cuotas, monto):
        primer_cuota = (monto * 1.08) / cuotas
        self._saldo = self._saldo - (primer_cuota)
        
#cuenta_billetera_virtual = Billetera("Juan Carlos")
#cuenta_billetera_virtual.pagar_debito(10)