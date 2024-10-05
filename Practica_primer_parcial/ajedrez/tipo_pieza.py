from Pieza import Pieza
# blancas

class peon(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("peon","vivo", color, ubicacion)
    def posibles_movimientos(self):
        print("adelante adelante")
    def mover(self):
        pass
    def comer(self):
        pass


class torre(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("torre","vivo", color, ubicacion)

class caballo(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("caballo","vivo", color, ubicacion)

class alfil(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("alfil","vivo", color, ubicacion)

class reina(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("reaina","vivo", color, ubicacion)

class rey(Pieza):
    def __init__(self, color, ubicacion):
        super().__init__("rey","vivo", color, ubicacion)
        