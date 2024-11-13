from Tienda import Tienda
from JuegoFisico import JuegoFisico

class VentaFisica(Tienda):
    
    def crearVenta(self, precio):
        return JuegoFisico(precio)