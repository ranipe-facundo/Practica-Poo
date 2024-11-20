from Bebida import Bebida

# Clase concreta Cafe que implementa Bebida
class Cafe(Bebida):

    def get_descripcion(self):
        return "Café"

    def get_costo(self):
        return 50.0

    def imprimir (self):
        print (self.get_costo())