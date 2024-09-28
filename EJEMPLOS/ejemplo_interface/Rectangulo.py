from Figura_clase_abstracta import Figura
from Calculos_interface import Calculos

class Rectangulo(Figura,Calculos): #le doy herencia de la clase abstracta y de la interface
    def __init__(self, alto, ancho, color):
        super().__init__(alto, ancho) #uso el constructor de clase abstracta
        self.__color = color #le agrego un parametro nuevo y lo pongo en oculto
    
    # le doy cuerpo a lo establecido en la interface
    def _calcular_area(self):
        return self._alto * self._alto
    
    def _calcular_perimetro(self):
        return self._alto + self._ancho
    
    def _imprimir(self):
        print (f"Nombre: Cuadrado")
        print (f"Color: {self.__color}")
        print (f"Alto: {self._alto}cm")
        print (f"Ancho: {self._ancho}cm")


# Este seria el main

cuadrado_rojo = Rectangulo(5,7,"Rojo")

cuadrado_rojo._imprimir()