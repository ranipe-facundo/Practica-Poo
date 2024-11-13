from CineFacade import CineFacade

class CineFacadeFacade:
    
    def __init__(self):
        self.__uso = CineFacade()

    # Método que combina todas las operaciones complejas en una sola llamada
    def uso(self, asiento, volumen):
        self.__uso.iniciarCine(asiento,volumen)
        self.__uso.apagarCine()