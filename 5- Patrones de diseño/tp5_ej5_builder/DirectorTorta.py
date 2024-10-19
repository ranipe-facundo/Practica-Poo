class DirectorDeTorta:
    def __init__(self, constructor_de_torta):
        self.__constructor_de_torta = constructor_de_torta
    
    def construir_torta_vainilla(self):
        self.__constructor_de_torta.crear_torta()
        self.__constructor_de_torta.agregar_masa()
        self.__constructor_de_torta.agregar_relleno()
    
    def construir_torta_coco(self):
        self.__constructor_de_torta.crear_torta()
        self.__constructor_de_torta.agregar_masa()
        self.__constructor_de_torta.agregar_relleno()
    
    def get_torta(self):
        return self.__constructor_de_torta.get_torta()