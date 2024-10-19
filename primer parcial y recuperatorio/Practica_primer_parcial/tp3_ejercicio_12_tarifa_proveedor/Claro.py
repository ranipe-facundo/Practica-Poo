from TarifaProveedor import TarifaProveedor

class Caro(TarifaProveedor):
    def __init__(self, nombre_proveedor, sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor, sms_usados, minutos_usados, gigas_usados)
    
    def get_nombre(self):
        return "Claro"

    def calcular(self):
        return super().calcular() * 1.2

# Claro: que tiene un 20% extra sobre el básico total