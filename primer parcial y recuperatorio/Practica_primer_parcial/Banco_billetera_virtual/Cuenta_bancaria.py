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
        if cantidad_cuotas <= 3:
            cuota = monto_a_pagar/cantidad_cuotas
            if cuota > self._saldo:
                print("Saldo insuficiente.")
            else:
                self._saldo = self._saldo - cuota
        else:
            interes = 0.02 * cantidad_cuotas
            valor_con_interes = monto_a_pagar * (1 + interes)
            cuota = valor_con_interes/cantidad_cuotas
            if cuota > self._saldo:
                print("Saldo insuficiente.")
            else:
                self._saldo = self._saldo - (cuota)
    
    def imprimir(self):
        super().imprimir()
        print(f"CBU: {self.__cbu}")