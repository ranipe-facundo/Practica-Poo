from Personal import Personal

class Docecente(Personal):
    def __init__(self, nombre_completo, antigüedad_años, sector):
        super().__init__(nombre_completo, antigüedad_años, sector)
        
    def calcula_cantidad_horas (self):
        if self._categoria == "simple":
            return 10
        if self._categoria == "semiexclusiva":
            return 20
        if self._categoria == "exclusiva":
            return 40

