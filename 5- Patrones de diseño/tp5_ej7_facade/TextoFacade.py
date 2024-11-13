from Convertidor import Convertidor
from Traductor import Traductor

class TextoFacade:
    
    def __init__(self):
        self.__traductor = Traductor()
        self.__convertidor = Convertidor()
    
    def traductor(self, palabra):
        self.__traductor.tracucir(palabra)
    
    def pasar_a_mayuscula(self, cadena):
        self.__convertidor.a_mayusculas(cadena)
    
    def pasar_a_minuscula(self, cadena):
        self.__convertidor.a_minusculas(cadena)