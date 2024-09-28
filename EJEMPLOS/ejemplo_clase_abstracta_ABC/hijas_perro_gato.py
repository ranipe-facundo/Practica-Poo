from Animal_ABC_padre import Animal

# Clase Perro que hereda de Animal
class Perro(Animal):
    
    def __init__(self, nombre, edad, color, raza):
        super().__init__(nombre, edad, color)
        self._raza = raza  # Atributo específico de Perro

    # Implementación del método abstracto
    def hacer_sonido(self):
        print(f"{self._nombre} dice: Guau guau!")

# Clase Gato que hereda de Animal
class Gato(Animal):
    
    def __init__(self, nombre, edad, color, pelo_largo):
        super().__init__(nombre, edad, color)
        self._pelo_largo = pelo_largo  # Atributo específico de Gato

    # Implementación del método abstracto
    def hacer_sonido(self):
        print(f"{self._nombre} dice: Miau!")