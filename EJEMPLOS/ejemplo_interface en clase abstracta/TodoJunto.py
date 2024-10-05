from abc import ABC, abstractmethod

# Interfaz que define los métodos abstractos para cálculos
class Calculos(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass

# Clase abstracta Figura que hereda de Calculos
class Figura(Calculos, ABC):
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    
        # Implementación del cálculo del área
    def calcular_area(self):
        return self._alto * self._ancho
    
    # Implementación del cálculo del perímetro
    def calcular_perimetro(self):
        return 2 * (self._alto + self._ancho)
    
    # Método de impresión común para todas las figuras
    def imprimir(self):
        print("Detalles de la figura:")
        print(f"Alto: {self._alto}cm")
        print(f"Ancho: {self._ancho}cm")

# Clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, alto, ancho, color):
        super().__init__(alto, ancho)
        self.__color = color
    
    # Sobrescribir el método de imprimir para incluir color y cálculos específicos
    def imprimir(self):
        super().imprimir()  # Llama al método de impresión de la clase base
        print(f"Color: {self.__color}")
        print(f"Área: {self.calcular_area()} cm^2")
        print(f"Perímetro: {self.calcular_perimetro()} cm")

# Main
rectangulo_rojo = Rectangulo(5, 7, "Rojo")
rectangulo_rojo.imprimir()