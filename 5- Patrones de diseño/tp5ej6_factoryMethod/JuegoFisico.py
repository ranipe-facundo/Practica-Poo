from Juego import Juego

class JuegoFisico(Juego):
    def __init__(self, precio):
        super().__init__(precio)
        self.__precioTraslado = 10
        self._precio_final = self.getPrecio()
    
    def getPrecio(self):
        return self.__precioTraslado + self._precio
    
    def imprimir(self):
        print("Este es un juego fisico")
        super().imprimir()
        print(f'Precio final: ${self._precio_final}')