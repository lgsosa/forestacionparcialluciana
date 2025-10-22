from .riego_strategy import RiegoStrategy
class RiegoAspersion(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 1.1)  # 10% extra por perdidas
