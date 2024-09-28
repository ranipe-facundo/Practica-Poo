from clase_padre import Arte

#Clase Derivada: Pintura
#La clase Pintura hereda de Arte y añade atributos específicos relacionados con pinturas, como el año de creación y el tipo de pintura.

class Pintura(Arte):
    def __init__(self, titulo, artista, ano_creacion, tipo_pintura):
        super().__init__(titulo, artista)
        self.ano_creacion = ano_creacion
        self.tipo_pintura = tipo_pintura

    def obtener_info(self):
        base_info = super().obtener_info()
        return f"{base_info}, Año de Creación: {self.ano_creacion}, Tipo de Pintura: {self.tipo_pintura}"

# Clase Derivada: Escultura
# La clase Escultura también hereda de Arte, pero agrega atributos específicos para esculturas, como el material y las dimensiones.

class Escultura(Arte):
    def __init__(self, titulo, artista, material, dimensiones):
        super().__init__(titulo, artista)
        self.material = material
        self.dimensiones = dimensiones

    def obtener_info(self):
        base_info = super().obtener_info()
        return f"{base_info}, Material: {self.material}, Dimensiones: {self.dimensiones}"

#Explicación del Rol de Cada Clase y la Implementación
#Clase Base Arte:

#Rol: Actúa como la clase general para todas las obras de arte en la galería. Define los atributos y métodos comunes, como el título y el artista.
#Motivo: Permite centralizar la información y los métodos comunes a todas las obras de arte. Facilita la extensión de la jerarquía de clases para incluir diferentes tipos de arte sin duplicar el código.
#Clase Derivada Pintura:

#Rol: Representa una pintura específica en la galería. Hereda de Arte y añade atributos adicionales relevantes para pinturas, como el año de creación y el tipo de pintura.
#Motivo: Permite especializar Arte para pinturas, agregando atributos específicos sin modificar la clase base. Utiliza el método super() para incluir la información general de la clase base.
#Clase Derivada Escultura:

#Rol: Representa una escultura específica en la galería. Hereda de Arte y añade atributos relevantes para esculturas, como el material y las dimensiones.
#Motivo: Proporciona una especialización de Arte para esculturas. Mantiene el código modular y reutilizable, permitiendo que cada tipo de obra tenga sus propios atributos específicos.
#Conclusión
#La herencia simple en este ejemplo permite organizar las obras de arte en la galería de manera eficiente. La clase base Arte proporciona una estructura común para todas las obras, mientras que las clases derivadas Pintura y Escultura permiten agregar información específica sin duplicar el código. Esto facilita la gestión y extensión del sistema a medida que se añaden nuevos tipos de obras de arte.







