from Agua import Agua
from Hierba import Hierba
from Fuego import Fuego
from Entrenador import Entrenador
import random

def pokemon_random():
    pokemon_agua = Agua(f"Pokemon_agua")
    pokemon_hierba = Hierba(f"Pokemon_hierba")
    pokemon_fuego = Fuego(f"Pokemon_fuego")
    lista = [pokemon_agua, pokemon_hierba, pokemon_fuego]
    return random.choice(lista)

lista_pokemon_salvajes = []

for i in range(10):
    lista_pokemon_salvajes.append(pokemon_random())

entrenador = Entrenador("Ash", random.randint(0,100), pokemon_random())

for i in lista_pokemon_salvajes:
    entrenador.atrapar_pokemon(i)

entrenador.imprimir()