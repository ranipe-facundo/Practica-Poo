from Personaje import Personaje

class Guerrero_paladin (Personaje):
    def __init__(self):
        super().__init__(nombre = "Paladin", vida = 100, nivelAtaque = 40, nivelDefensa = 40)
    
    def atacar (self):
        return self._nivelAtaque * 1.1 # aca extenderia en el metodo atacar
    def defender(self):
        return self._nivelDefensa

class Guerrero_barbaro (Personaje):
    def __init__(self):
        super().__init__(nombre = "Barbaro", vida = 150, nivelAtaque = 50, nivelDefensa = 5)
        
    def atacar (self):
        return self._nivelAtaque * 1.3 # aca extenderia en el metodo atacar
    def defender(self):
        return self._nivelDefensa
    
# Definir la excepción personalizada
class numero_negativo(Exception):
    pass

# Función que puede lanzar la excepción
def verificar_numero(numero):
    if numero <= 0:
        raise numero_negativo
    return numero

barbaro1 = Guerrero_barbaro()
paladin1 = Guerrero_paladin()

def pelea_por_turnos (guerrero1, guerrero2):
    def imprimir_vidas():
        print(f"Vida del {guerrero1._nombre}: {guerrero1._vida}\nVida del {guerrero2._nombre}: {guerrero2._vida}")
    numero_turno = 1
    while guerrero1._vida >= 0 and guerrero2._vida >= 0:
        print(f"Turno {numero_turno}")
        numero_turno += 1
        try:
            guerrero1.ataca_a(guerrero2)
            verificar_numero(guerrero2._vida)
        except numero_negativo:
            guerrero2._vida = 0
            print(f"El guerrero {guerrero2._nombre} quedo fuera de combate!")
            break
        #if guerrero2.get_vida == 0:
        try:
            guerrero2.ataca_a(guerrero1)
            verificar_numero(guerrero2._vida)
        except numero_negativo:
            guerrero1._vida = 0
            print(f"El guerrero {guerrero2._nombre} quedo fuera de combate!")
            break
        imprimir_vidas()
    imprimir_vidas()
pelea_por_turnos(barbaro1,paladin1)