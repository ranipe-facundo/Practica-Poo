class Puesto:
    def __init__(self,nombre_puesto):
        self.__nombre_puesto = nombre_puesto
    
    def get_nombre_puesto (self, nombre_puesto):
        self.__nombre_puesto = nombre_puesto
    def get_nombre_puesto (self):
        return self.__nombre_puesto