from Tienda import Tienda
from JuegoDigital import JuegoDigital

class VentaDigital(Tienda):
    
    def crearVenta(self, precio, plataforma):
        return JuegoDigital(precio, plataforma)
    