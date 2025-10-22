from abc import ABC, abstractmethod

class Cultivo(ABC):
    def __init__(self, nombre: str, consumo_agua_litros: float):
        self.nombre = nombre
        self.consumo_agua_litros = consumo_agua_litros

    @abstractmethod
    def tipo(self) -> str:
        ...

    def __str__(self) -> str:
        return f"{self.tipo()}({self.nombre}, {self.consumo_agua_litros}L)"
