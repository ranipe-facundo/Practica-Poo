import random

# Lista de ejemplo
lista = ['manzana', 'banana', 'naranja', 'pera', 'uva']

# Usar random.choice() para seleccionar un elemento aleatorio
eleccion_aleatoria = random.choice(lista)
print(f"Elemento aleatorio con choice: {eleccion_aleatoria}")

# Usar random.sample() para seleccionar 3 elementos aleatorios sin repetición
muestra_aleatoria = random.sample(lista, 3)
print(f"Elementos aleatorios con sample: {muestra_aleatoria}")

# Lista original de 22 elementos
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Dividir la lista en dos listas de 11 elementos cada una
lista1 = lista_original[:11]
lista2 = lista_original[11:]

print("Lista 1:", lista1)
print("Lista 2:", lista2)