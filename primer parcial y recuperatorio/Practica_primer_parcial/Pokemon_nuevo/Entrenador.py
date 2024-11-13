
class Entrenador:
    def __init__(self, nombre, nivel_entrenador, pokemon_principal):
        self.__nombre = nombre
        self.__nivel_entrenador = nivel_entrenador
        self.__pokemon_principal = pokemon_principal
        self.__pokedex = []
        
    def atrapar_pokemon(self, pokemon_salvaje):
        salvajismo_enemigo = pokemon_salvaje.get_salvajismo()
        if self.__nivel_entrenador > salvajismo_enemigo:
            self.__pokedex.append(pokemon_salvaje)
            print("El pokemon se ah capturado con éxito!")
        else:
            for i in range (3):
                ataque = self.__pokemon_principal.ataque(pokemon_salvaje)
                pokemon_salvaje.defensa(ataque)
                salvajismo_enemigo = salvajismo_enemigo - (salvajismo_enemigo * 0.1)
                if pokemon_salvaje.get_vida() <= 0:
                    print("El pokemon se ah debilitado, no se pudo capturar.")
                    break
                if self.__nivel_entrenador > salvajismo_enemigo:
                    self.__pokedex.append(pokemon_salvaje)
                    print("El pokemon se ah capturado con éxito!")
                    break
            print("Se hicieron los 3 ataques y el pokemon ah escapado.")
    
    def imprimir(self): # en el ejercicio no dice que se tiene que establecer un imprimir para el entrenador, lo pide en la simulacion, pero el profesor lo hace así en su resolucion
        print("=======================")
        print(f"Nombre del entrenador: {self.__nombre}")
        print(f"Nivel del entrenador: {self.__nivel_entrenador}")
        for i in self.__pokedex:
            print("-----------------------")
            i.imprimir()