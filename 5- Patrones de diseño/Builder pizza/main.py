from Cook_Director import Cook
from Pizza_Builder import MargheritaBuilder

#se instancia la clase director
cook = Cook()
# se instancia los constructores de los diferentes bulders
margherita_builder = MargheritaBuilder()

# ahora se puede mandar a llamar la clase directora y recibir objetos tipo Pizza

pizza  = cook.make_pizza(margherita_builder)

print(pizza)