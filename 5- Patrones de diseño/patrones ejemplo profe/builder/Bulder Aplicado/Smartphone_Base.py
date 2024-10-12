#CLASE BASE
from typing import Any

class Smartphone():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del smartphone: {', '.join(self.parts)}", end="")