from abc import ABC, abstractmethod

class Tienda(ABC):#tienda 
    
    @abstractmethod
    def crearVenta (self): #este es el factory method
        pass
    
    
    """
    def realizar_compra(self):
        enviarJuego = self._crearCompra() <--- logica extra propia del ejercicio, en este no haría falta
        enviarJuego.entregar()
        """ 