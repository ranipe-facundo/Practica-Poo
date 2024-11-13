class Paquete():
    def __init__(self, peso, alto, ancho, longitud):
        self.__peso = peso
        self.__alto = alto
        self.__ancho = ancho
        self.__longitud = longitud
        
    def getPeso(self):
        return self.__peso
        
    def pesoVolumetrico(self):
        return (self.__alto * self.__ancho * self.__longitud) / 5000
        
    def __str__(self):
        return (f'Peso: {self.__peso}\n'
                f'Alto: {self.__alto}\n'
                f'Ancho: {self.__ancho}\n'
                f'longitud: {self.__longitud}')
