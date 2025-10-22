from abc import ABC, abstractmethod

class RiegoStrategy(ABC):
    @abstractmethod
    def regar(self, litros_disponibles: float, consumo_por_cultivo: float) -> float:
        """Devuelve litros restantes tras regar un cultivo."""
        ...

# Esto lo hice para poder cambiar el tipo de riego (goteo o aspersión) cuando quiera.
