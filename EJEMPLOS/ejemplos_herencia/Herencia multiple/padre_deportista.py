class Deportista:
    def __init__(self, deporte, nivel_entrenamiento):
        self.deporte = deporte
        self.nivel_entrenamiento = nivel_entrenamiento

    def entrenar(self):
        self.nivel_entrenamiento += 1
        return f"Entrenando en {self.deporte}, nivel actual: {self.nivel_entrenamiento}"
