# Director
from Pizza_Builder import MargheritaBuilder

class Cook:
    def make_pizza (self, builder):
        builder.set_dough()
        builder.set_sauce()
        builder.set_topping()
        return  builder.pizza 