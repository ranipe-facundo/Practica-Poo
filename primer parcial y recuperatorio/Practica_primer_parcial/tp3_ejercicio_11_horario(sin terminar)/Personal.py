from abc import ABC, abstractmethod

class Personal (ABC):
    def __init__(self,nombre_completo,antigüedad_años,sector):
        self._nombre_completo = nombre_completo
        self._antigüedad_años = antigüedad_años
        self._sector = sector
        self._categoria = ""
        self._cantidad_horas_semanales = self.calcula_cantidad_horas()
        
    @abstractmethod
    def calcula_cantidad_horas (self):
        pass