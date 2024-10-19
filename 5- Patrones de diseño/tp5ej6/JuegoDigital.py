from Juego import Juego

class JuegoDigital(Juego):
    def __init__(self, precio, plataforma):
        super().__init__(precio)
        self.__plataforma = plataforma
    
    def getPrecio(self, plataforma):
        if self.__plataforma == "Steam":
            return self._precio * 1.1
        if self.__plataforma == "Epic":
            return self._precio * 1.15
