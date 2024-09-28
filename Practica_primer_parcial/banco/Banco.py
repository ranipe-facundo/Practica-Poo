from Cuenta import Cuenta
import random

class Banco(Cuenta):
    def __init__(self, dueno):
        super().__init__(dueno)
    
        self.__cbu = random.randint(100,9999)
        
    
    def pagar_debito(self,monto):
        self._saldo = self._saldo - (monto - (monto * 0.1))
    
    def pagar_credito(self,cuotas,monto):
        if cuotas > 3:
            monto = monto * ((0.02*cuotas) +1 )
        descontar_cuota = monto / cuotas
        self._saldo = self._saldo - descontar_cuota