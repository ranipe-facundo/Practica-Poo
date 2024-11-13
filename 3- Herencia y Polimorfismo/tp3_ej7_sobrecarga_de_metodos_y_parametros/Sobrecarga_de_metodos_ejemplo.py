class Calculadora:
    def sumar(self, a, b=0, c=0):
        """
        Método para sumar. Funciona con dos o tres argumentos.
        """
        return a + b + c

# Crear una instancia de la clase Calculadora
calc = Calculadora()

# Llamadas al método sumar con diferentes números de argumentos
resultado1 = calc.sumar(5, 10)     # Suma dos números
resultado2 = calc.sumar(5, 10, 20) # Suma tres números
resultado3 = calc.sumar(5)         # Suma uno más el valor por defecto del segundo argumento

print(f"Resultado 1: {resultado1}")  # Resultado: 15
print(f"Resultado 2: {resultado2}")  # Resultado: 35
print(f"Resultado 3: {resultado3}")  # Resultado: 5