from Componente import Componente

class Carpeta(Componente):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__elementos = []
    
    def es_carpeta(self):
        return True
    
    def agregar_elemnto(self,elemento):
        self.__elementos.append(elemento)

    def imprimir(self):
        print(f'{self.__nombre}')
        for elemento in self.__elementos:
            elemento.imprimir()