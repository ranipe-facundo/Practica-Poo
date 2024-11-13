from abc import ABC

class Tarifa_proveedor(ABC):
    def __init__(self, nombre_proveedor, sms_usados, minutos_usados, gigas_usados):
        self.__nombre_proveedor = nombre_proveedor
        self.__sms_usados = sms_usados
        self.__minutos_usados = minutos_usados
        self.__gigas_usados = gigas_usados
    
    def get_nombre_proveedor (self):
        return self.__nombre_proveedor
    def get_sms_usados (self):
        return self.__sms_usados
    def get_minutos_usados (self):
        return self.__minutos_usados
    def get_gigas_usados (self):
        return self.__gigas_usados
    
    def calcular(self,total_sms, total_minutos, total_gigas):
        return (total_sms + (total_minutos * 15) + (total_gigas * 20))
