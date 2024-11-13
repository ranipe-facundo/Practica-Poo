from Componente import Componente

class Archivo(Componente):
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def es_carpeta(self):
        return False
    
    def imprimir(self):
        print(self.__nombre)
