from abc import ABC,abstractmethod

class TarifaProveedor(ABC):
    def __init__(self, sms_usados, minutos_usados, gigas_usados):
        self._sms_usados = sms_usados
        self._minutos_llamada_usados = minutos_usados
        self._gigas_usados = gigas_usados
        
    def _calcular_SMS(self):
        return self._sms_usados * 1
    def _calcularMinutosDeLlamada(self):
        return self._minutos_llamada_usados * 15
    def _calcularConsumoGB(self):
        return self._gigas_usados * 20
        
    def calcular(self):
        return self._calcular_SMS() + self._calcularMinutosDeLlamada() + self._calcularConsumoGB()
    
    @abstractmethod
    def get_nombre(self):
        pass
