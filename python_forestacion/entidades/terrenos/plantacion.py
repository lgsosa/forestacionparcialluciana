from typing import List
from .terreno import Terreno
from ..cultivos.cultivo import Cultivo
from ...excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

class Plantacion:
    def __init__(self, terreno: Terreno, superficie_disponible_m2: float):
        if superficie_disponible_m2 > terreno.superficie_m2:
            raise SuperficieInsuficienteException("Superficie mayor que el terreno")
        self.terreno = terreno
        self.superficie_disponible_m2 = superficie_disponible_m2
        self.cultivos: List[Cultivo] = []

    def agregar_cultivo(self, cultivo: Cultivo):
        self.cultivos.append(cultivo)

    def __str__(self) -> str:
        return f"Plantacion ({self.terreno.nombre}, {len(self.cultivos)} cultivos)"
