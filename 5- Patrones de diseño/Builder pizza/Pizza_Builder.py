# Builder
from Pizza_Base_class import Pizza

class PizzaBuilder:
    def set_dough(self, dough):
        pass                    #Se va a definir en cada tipo de pizza
    
    def set_sauce(self, sauce):
        pass
    
    def set_topping(self, topping):
        pass

class MargheritaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def set_dough(self):
        self.pizza.dough = "Regular" 
    
    def set_sauce(self):
        self.pizza.sauce = "Tomate"
    
    def set_topping(self):
        self.pizza.topping = "Mozzarella"