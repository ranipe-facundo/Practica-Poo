class Torta():
    def __init__(self):
        self.__masa = None
        self.__relleno = None
    
    def set_masa(self, masa):
        self.__masa = masa
    
    def set_relleno(self, relleno):
        self.__relleno = relleno
    
    def imprimir(self):
        print("Caracteristicas de la torta:")
        print (f"Masa: {self.__masa}")
        print (f"Relleno: {self.__relleno}")