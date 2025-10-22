from ..entidades.terrenos.plantacion import Plantacion
from ..patrones.factory.cultivo_factory import crear_cultivo

class PlantacionService:
    """SRP:gestiona alta de cultivos para una plantación"""
    def __init__(self, plantacion: Plantacion):
        self.plantacion = plantacion

    def alta_cultivo(self, tipo: str, nombre: str, consumo: float):
        cultivo = crear_cultivo(tipo, nombre, consumo)  # OCP: nuevos tipos sin tocar este código
        self.plantacion.agregar_cultivo(cultivo)
        return cultivo
