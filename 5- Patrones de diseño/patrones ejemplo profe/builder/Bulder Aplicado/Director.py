#DIRECTOR

from Smartphone_Builder import BuilderSmartphone

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderSmartphone:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderSmartphone) -> None:
        self._builder = builder

    def build_basic(self) -> None:
        self.builder.produce_screen()
        self.builder.produce_network()

    def build_full(self) -> None:
        self.builder.produce_screen()
        self.builder.produce_network()
        self.builder.produce_bluetooth() 