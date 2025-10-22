from .riego_strategy import RiegoStrategy
class RiegoGoteo(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 0.8)  # 20% ahorro
