from Cuenta import Cuenta
import random

class Billetera_virtual(Cuenta):
    def __init__(self, duenio):
        super().__init__(duenio)
        self.__cvu = random.randint(0,999)

    def pagar_credito(self, monto_a_pagar, cantidad_cuotas):
            interes = ((cantidad_cuotas * 8) / 100) + 1
            monto_a_pagar = monto_a_pagar * interes
            self._saldo = self._saldo - (monto_a_pagar / cantidad_cuotas)
    
    def imprimir(self):
        super().imprimir()
        print(f"CVU: {self.__cvu}")