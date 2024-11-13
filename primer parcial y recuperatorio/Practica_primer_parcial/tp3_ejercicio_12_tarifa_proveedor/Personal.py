from TarifaProveedor import TarifaProveedor

class Personal(TarifaProveedor):
    def __init__(self, nombre_proveedor, sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor, sms_usados, minutos_usados, gigas_usados)
    
    def get_nombre(self):
        return "Personal"
    def _calcularMinutosDeLlamada(self):
        return super()._calcularMinutosDeLlamada() * 1.20
    def _calcularConsumoGB(self):
        return super()._calcularConsumoGB() * 1.5
    
