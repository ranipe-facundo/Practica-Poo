from Juego import Juego

class JuegoDigital(Juego):
    def __init__(self, precio, plataforma):
        super().__init__(precio)
        self.__plataforma = plataforma
        self._precio_final = self.getPrecio(plataforma) #este atributo no lo pide el ejercicio pero se me ocurrio ponerlo como para que imporima el precio total
        # No seria correcto usar un metodo publico para calcular el precio,
        #pero el ejercicio me pidio que getPrecio sea un metodo abstracto, así que lo uso para dar el precio final
        
    def getPrecio(self, plataforma):
        if self.__plataforma == "Steam":
            return self._precio * 1.1
        if self.__plataforma == "Epic":
            return self._precio * 1.15
    
    def imprimir(self):
        print("Este es un juego digital")
        super().imprimir()
        print(f'Plataforna: {self.__plataforma}')
        print(f'Precio final: ${self._precio_final:.2f}')


juego = JuegoDigital(40,"Steam")
