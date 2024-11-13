#Está mal tendria que ser una interface

from Casa import Casa
                        #  La interfaz Builder declara los pasos comunes a todos los builder.
class ConstructorDeCasa:
    def __init__(self):
        self._casa = None

    def get_casa(self): #Build
        return self._casa

    def crear_nueva_casa(self, nombre): #Reset
        self._casa = Casa(nombre)

    def construir_cimientos(self):
        raise NotImplementedError

    def construir_estructura(self):
        raise NotImplementedError

    def construir_techo(self):
        raise NotImplementedError

    def construir_garage(self):
        raise NotImplementedError

    def construir_piscina(self):
        raise NotImplementedError

    def construir_jardin(self):
        raise NotImplementedError
