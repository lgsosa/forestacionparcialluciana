from ..patrones.singleton.config import Config
from ..patrones.strategy.riego_strategy import RiegoStrategy
from ..excepciones.agua_agotada_exception import AguaAgotadaException
from ..excepciones.forestacion_exception import ForestacionException
from .. import constantes as K

# Este servicio se encarga solo del riego, así lo tengo separado de los demás.

class RiegoService:
    """DIP: depende de la abstracción RiegoStrategy, no de una implementación fija."""
    def __init__(self, strategy: RiegoStrategy):
        self.strategy = strategy
        self._ultima_temp = None
        self._ultima_hum = None

    # Los sensores notifican; estos setters simulan el 'update'
    def set_temp(self, temp): self._ultima_temp = temp
    def set_hum(self, hum): self._ultima_hum = hum

    def condiciones_habilitadas(self) -> bool:
        if self._ultima_temp is None or self._ultima_hum is None:
            return False
        return (K.TEMP_RIEGO_MIN <= self._ultima_temp <= K.TEMP_RIEGO_MAX) and (self._ultima_hum < K.HUMEDAD_UMBRAL)

    def regar_cultivo(self, consumo_por_cultivo: float):
        cfg = Config()
        if cfg.tanque_agua_litros < K.AGUA_MINIMA:
            raise AguaAgotadaException("Tanque por debajo del mínimo")
        litros_restantes = self.strategy.regar(cfg.tanque_agua_litros, consumo_por_cultivo)
        if litros_restantes < 0:
            raise ForestacionException("Consumo excede al tanque")
        cfg.tanque_agua_litros = litros_restantes
        return cfg.tanque_agua_litros
