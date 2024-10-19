from abc import ABC, abstractmethod

class Compra(ABC):#tienda 
    
    @abstractmethod
    def crearCompra (self): #este es el factory method
        pass
    
    
    """
    def realizar_compra(self):
        enviarJuego = self._crearCompra() <--- logica extra propia del ejercicio
        enviarJuego.entregar()
        """