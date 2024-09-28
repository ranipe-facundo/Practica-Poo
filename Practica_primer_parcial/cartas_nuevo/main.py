from Plantilla import Plantilla
from Bronce_especial import Bronce_especial
from Oro import Oro
from Especial import Especial
import random
from listas import Lista_clubes, Lista_paises

lista_jugadores = []

for i in range(22):
    oro = Oro(f"Jugador {i+1}", random.choice(Lista_clubes), random.choice(Lista_paises))
    especial = Especial(f"Jugador: {i+1}", random.choice(Lista_clubes), random.choice(Lista_paises))
    bronce_especial = Bronce_especial(f"jugador {i+1}", random.choice(Lista_clubes), random.choice(Lista_paises))
    lista = [oro, especial, bronce_especial]
    lista_jugadores.append(random.choice(lista))

random.shuffle(lista_jugadores)

equipo1 = Plantilla("Equipo 1", random.choice(Lista_paises), random.choice(Lista_clubes))
equipo2 = Plantilla("Equipo 2", random.choice(Lista_paises), random.choice(Lista_clubes))

plantilla1 = lista_jugadores [:11]
plantilla2 = lista_jugadores [11:]

equipo1.set_plantel(plantilla1)
equipo2.set_plantel(plantilla2)



equipo1.imprimir()
print("=================================")
equipo2.imprimir()
