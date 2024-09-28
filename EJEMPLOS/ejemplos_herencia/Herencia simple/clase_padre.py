# Ejemplo: Gestión de una Galería de Arte
# Clase Base: Arte
# Esta clase representa una obra de arte general en la galería, con atributos comunes a todas las obras, como el título y el artista.

class Arte:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def obtener_info(self):
        return f"Título: {self.titulo}, Artista: {self.artista}"
