from ConstructorDeTorta import ConstructorDeTorta
from Torta import Torta

class ConstructorDeTortaChocolate(ConstructorDeTorta):
    def __init__(self):
        self._torta = None
    
    def get_torta(self):
        return self._torta
    
    def crear_torta(self):
        self._torta = Torta()
    
    def agregar_masa(self):
        self._torta.set_masa("Chocolate") 

    def agregar_relleno(self):
        self._torta.set_relleno("Dulce de leche")