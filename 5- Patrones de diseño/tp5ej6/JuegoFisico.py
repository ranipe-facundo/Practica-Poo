from Juego import Juego

class JuegoFisico(Juego):
    def __init__(self, precio):
        super().__init__(precio)
        self.__precioTraslado = 10
    
    def getPrecio(self, plataforma):
        return self.__precioTraslado + self._precio