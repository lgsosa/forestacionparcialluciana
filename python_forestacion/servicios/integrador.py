"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/4: mensajes_service.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\mensajes_service.py
# ================================================================================

﻿class MensajesService:
    def info(self, msg: str): print(f"[INFO] {msg}")
    def warn(self, msg: str): print(f"[WARN] {msg}")
    def error(self, msg: str): print(f"[ERROR] {msg}")


# ================================================================================
# ARCHIVO 3/4: plantacion_service.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\plantacion_service.py
# ================================================================================

﻿from ..entidades.terrenos.plantacion import Plantacion
from ..patrones.factory.cultivo_factory import crear_cultivo

class PlantacionService:
    """SRP:gestiona alta de cultivos para una plantación"""
    def __init__(self, plantacion: Plantacion):
        self.plantacion = plantacion

    def alta_cultivo(self, tipo: str, nombre: str, consumo: float):
        cultivo = crear_cultivo(tipo, nombre, consumo)  # OCP: nuevos tipos sin tocar este código
        self.plantacion.agregar_cultivo(cultivo)
        return cultivo


# ================================================================================
# ARCHIVO 4/4: riego_service.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\riego_service.py
# ================================================================================

﻿from ..patrones.singleton.config import Config
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


