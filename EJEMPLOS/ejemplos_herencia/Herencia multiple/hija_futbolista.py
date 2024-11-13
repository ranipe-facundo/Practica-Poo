from padre_deportista import Deportista
from padre_empleado import Empleado

class FutbolistaProfesional(Empleado, Deportista):
    def __init__(self, nombre, salario, deporte, nivel_entrenamiento, posicion):
        Empleado.__init__(self, nombre, salario)
        Deportista.__init__(self, deporte, nivel_entrenamiento)
        self.posicion = posicion

    def jugar_partido(self):
        return f"{self.nombre}, quien juega como {self.posicion}, está jugando un partido de {self.deporte}."

    def obtener_info(self):
        salario_anual = self.calcular_salario_anual()
        entreno = self.entrenar()
        return f"Nombre: {self.nombre}, Salario Anual: {salario_anual}, {entreno}, Posición: {self.posicion}"

futbolista = FutbolistaProfesional(nombre="Juan Pérez", salario=3000, deporte="Fútbol", nivel_entrenamiento=5, posicion="Delantero")

print(futbolista.jugar_partido())
print(futbolista.obtener_info())
