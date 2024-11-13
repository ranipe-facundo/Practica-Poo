from Director import Director
from Smartphone_Builder import ConcreteBuilderSmartphone


director = Director()
builder = ConcreteBuilderSmartphone()
director.builder = builder

print("Smartphone basico: ")
director.build_basic()
builder.smartphone.list_parts()

print("\n")

print("Smartphone alta gama: ")
director.build_full()
builder.smartphone.list_parts()