from TarifaProveedor import TarifaProveedor

class Movistar(TarifaProveedor):
    def __init__(self, nombre_proveedor, sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor, sms_usados, minutos_usados, gigas_usados)
    
    def get_nombre(self):
        return "Movistar"
    
    def _calcular_SMS(self):
        return super()._calcular_SMS() *1.1
    def _calcularMinutosDeLlamada(self):
        return super()._calcularMinutosDeLlamada() *1.2
    def _calcularConsumoGB(self):
        return super()._calcularConsumoGB() *1.3

    #Movistar: tiene un 10% extra sobre los mensajes de texto, 20% sobre las
    #llamadas y 30% sobre los GB de datos.