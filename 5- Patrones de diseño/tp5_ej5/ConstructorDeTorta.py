from Torta import Torta

class ConstructorDeTorta:
    def __init__(self):
        self._torta = None
    
    def get_torta(self):
        return self._torta
    
    def crear_nueva_torta(self, nombre):
        self._torta = Torta(nombre)
    
    def set_relleno(self, relleno):
        pass
    
    def set_masa(self, masa):
        pass
    
#    def set_relleno(self):
#        raise NotImplementedError
#                                       <-- Creo que esto se usaria si estoy agregando parametros que podria tener o no la torta
#    def set_masa(self):
#        raise NotImplementedError