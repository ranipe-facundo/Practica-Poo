from Cuenta import Cuenta
import random

class Cuenta_Bancaria(Cuenta):
    def __init__(self, duenio):
        super().__init__(duenio)
        self.__cbu = random.randint(0,999)
    
    def pago_debito(self, monto_a_debitar):
        super().pago_debito(monto_a_debitar)
        renintegro = monto_a_debitar * 0.1
        self._saldo = self._saldo + renintegro

    def pagar_credito(self, monto_a_pagar, cantidad_cuotas):
        if cantidad_cuotas <= 3
            self._saldo = self._saldo - (monto_a_pagar/cantidad_cuotas)
        else:
            interes 
            
            
            interes = 
            monto_a_pagar = monto_a_pagar * interes