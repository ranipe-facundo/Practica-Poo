# Clase base
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

# Clase derivada Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

# Clase derivada Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

# Función que utiliza polimorfismo
def imprimir_sonido(animal):
    print(animal.hacer_sonido())

# Crear instancias de Perro y Gato
mi_perro = Perro()
mi_gato = Gato()

# Llamar al método hacer_sonido usando polimorfismo
imprimir_sonido(mi_perro)  # Imprime: Guau guau
imprimir_sonido(mi_gato)   # Imprime: Miau miau
