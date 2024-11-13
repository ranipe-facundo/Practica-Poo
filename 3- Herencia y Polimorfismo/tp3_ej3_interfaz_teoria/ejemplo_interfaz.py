from abc import ABC, abstractmethod #módulo abc es Abstract Base Classes

# Definición de la interfaz mediante una clase abstracta
class Dispositivo(ABC):
    
    # Método abstracto: todas las clases que implementen esta interfaz deben definirlo
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

# Implementación de la interfaz en una clase concreta
class Telefono(Dispositivo):
    def encender(self):
        print("El teléfono se ha encendido.")
    
    def apagar(self):
        print("El teléfono se ha apagado.")

# Otra implementación de la interfaz
class Computadora(Dispositivo):
    def encender(self):
        print("La computadora se ha encendido.")
    
    def apagar(self):
        print("La computadora se ha apagado.")

# Uso
telefono = Telefono()
telefono.encender()  # Llamada al método implementado en Telefono
telefono.apagar()

computadora = Computadora()
computadora.encender()  # Llamada al método implementado en Computadora
computadora.apagar()