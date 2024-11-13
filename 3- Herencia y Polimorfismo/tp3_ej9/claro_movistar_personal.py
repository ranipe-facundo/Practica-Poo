from tarifa_proveedor import Tarifa_proveedor

class Claro (Tarifa_proveedor):
    def __init__(self,sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor= "Claro", sms_usados = sms_usados,minutos_usados = minutos_usados, gigas_usados = gigas_usados) # claro lleva un 20% del base total
    
    def calcular(self,total_sms, total_minutos, total_gigas):
        return ((total_sms + (total_minutos * 15) + (total_gigas * 20)) * 1.2)
    
class Movistar (Tarifa_proveedor):
    def __init__(self, sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor = "Movistar", sms_usados = sms_usados * 1.2, minutos_usados = minutos_usados * 1.5, gigas_usados = gigas_usados)
        
class Personal (Tarifa_proveedor):
    def __init__(self, sms_usados, minutos_usados, gigas_usados):
        super().__init__(nombre_proveedor = "Personal", sms_usados = sms_usados * 1.1 , minutos_usados = minutos_usados * 1.2, gigas_usados = gigas_usados * 1.3)

claro1 = Claro(50, 100, 5)
movistar1 = Movistar(50, 100,5)
personal1 = Personal(50, 100,5)

print(f" El total de la factura {claro1.get_nombre_proveedor()} es de {claro1.calcular(claro1.get_sms_usados(),claro1.get_minutos_usados(), claro1.get_gigas_usados())} pesos.")