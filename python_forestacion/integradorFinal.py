"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion
Fecha de generacion: 2025-10-22 10:52:25
Total de archivos integrados: 37
Total de directorios procesados: 13
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   4. __init__.py
#   5. cultivo.py
#   6. lechuga.py
#   7. olivo.py
#   8. pino.py
#   9. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   10. __init__.py
#   11. operario.py
#
# DIRECTORIO: entidades\terrenos
#   12. __init__.py
#   13. plantacion.py
#   14. terreno.py
#
# DIRECTORIO: excepciones
#   15. __init__.py
#   16. agua_agotada_exception.py
#   17. forestacion_exception.py
#   18. mensajes_exception.py
#   19. persistencia_exception.py
#   20. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   21. __init__.py
#
# DIRECTORIO: patrones\factory
#   22. __init__.py
#   23. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   24. __init__.py
#   25. observer.py
#
# DIRECTORIO: patrones\singleton
#   26. __init__.py
#   27. config.py
#
# DIRECTORIO: patrones\strategy
#   28. __init__.py
#   29. riego_aspersion.py
#   30. riego_goteo.py
#   31. riego_strategy.py
#
# DIRECTORIO: riego
#   32. __init__.py
#   33. sensor.py
#
# DIRECTORIO: servicios
#   34. __init__.py
#   35. mensajes_service.py
#   36. plantacion_service.py
#   37. riego_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/37: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 2/37: constantes.py
# Directorio: .
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\constantes.py
# ==============================================================================

﻿TEMP_RIEGO_MIN = 8
TEMP_RIEGO_MAX = 15
HUMEDAD_UMBRAL = 50
AGUA_MINIMA = 10



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/37: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\__init__.py
# ==============================================================================

﻿



################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/37: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 5/37: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

﻿from abc import ABC, abstractmethod

class Cultivo(ABC):
    def __init__(self, nombre: str, consumo_agua_litros: float):
        self.nombre = nombre
        self.consumo_agua_litros = consumo_agua_litros

    @abstractmethod
    def tipo(self) -> str:
        ...

    def __str__(self) -> str:
        return f"{self.tipo()}({self.nombre}, {self.consumo_agua_litros}L)"


# ==============================================================================
# ARCHIVO 6/37: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

﻿from .cultivo import Cultivo
class Lechuga(Cultivo):
    def tipo(self) -> str: return "Lechuga"


# ==============================================================================
# ARCHIVO 7/37: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

﻿from .cultivo import Cultivo
class Olivo(Cultivo):
    def tipo(self) -> str: return "Olivo"


# ==============================================================================
# ARCHIVO 8/37: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

﻿from .cultivo import Cultivo
class Pino(Cultivo):
    def tipo(self) -> str: return "Pino"


# ==============================================================================
# ARCHIVO 9/37: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

﻿from .cultivo import Cultivo
class Zanahoria(Cultivo):
    def tipo(self) -> str: return "Zanahoria"



################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 10/37: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\personal\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 11/37: operario.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\personal\operario.py
# ==============================================================================

﻿class Operario:
    def __init__(self, nombre: str):
        self.nombre = nombre



################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 12/37: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 13/37: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

﻿from typing import List
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


# ==============================================================================
# ARCHIVO 14/37: terreno.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\terreno.py
# ==============================================================================

﻿class Terreno:
    def __init__(self, nombre: str, superficie_m2: float):
        self.nombre = nombre
        self.superficie_m2 = superficie_m2



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 15/37: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 16/37: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

﻿from .forestacion_exception import ForestacionException
class AguaAgotadaException(ForestacionException):
    pass


# ==============================================================================
# ARCHIVO 17/37: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

﻿class ForestacionException(Exception):
    """Excepcion base del dominio."""
    pass


# ==============================================================================
# ARCHIVO 18/37: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

﻿from .forestacion_exception import ForestacionException
class MensajesException(ForestacionException):
    pass


# ==============================================================================
# ARCHIVO 19/37: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

﻿from .forestacion_exception import ForestacionException
class PersistenciaException(ForestacionException):
    pass


# ==============================================================================
# ARCHIVO 20/37: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

﻿from .forestacion_exception import ForestacionException
class SuperficieInsuficienteException(ForestacionException):
    pass



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 21/37: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\__init__.py
# ==============================================================================

﻿



################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 22/37: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\factory\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 23/37: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

﻿from ...entidades.cultivos.pino import Pino
from ...entidades.cultivos.olivo import Olivo
from ...entidades.cultivos.lechuga import Lechuga
from ...entidades.cultivos.zanahoria import Zanahoria
from ...entidades.cultivos.cultivo import Cultivo

def crear_cultivo(tipo: str, nombre: str, consumo: float) -> Cultivo:
    t = tipo.lower()
    if t == "pino":      return Pino(nombre, consumo)
    if t == "olivo":     return Olivo(nombre, consumo)
    if t == "lechuga":   return Lechuga(nombre, consumo)
    if t == "zanahoria": return Zanahoria(nombre, consumo)
    raise ValueError(f"Tipo de cultivo desconocido: {tipo}")

# Hice esta función para crear los cultivos según el tipo.
# Así no tengo que andar poniendo muchos "if" en otros lados.



################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 24/37: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\observer\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 25/37: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\observer\observer.py
# ==============================================================================

﻿class Subject:
    def __init__(self):
        self._obs = []

    def suscribir(self, o):
        self._obs.append(o)

    def notificar(self, dato):
        for o in self._obs:
            o.update(dato)

class Observer:
    def update(self, dato):
        ...



################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 26/37: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\singleton\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 27/37: config.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\singleton\config.py
# ==============================================================================

﻿class _Config:
    def __init__(self):
        self.tanque_agua_litros = 100  # stock inicial

class Config:
    _inst = None
    def __new__(cls):
        if cls._inst is None:
            cls._inst = _Config()
        return cls._inst

# Uso una sola instancia para el tanque de agua así no se mezclan los valores.



################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 28/37: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 29/37: riego_aspersion.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_aspersion.py
# ==============================================================================

﻿from .riego_strategy import RiegoStrategy
class RiegoAspersion(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 1.1)  # 10% extra por perdidas


# ==============================================================================
# ARCHIVO 30/37: riego_goteo.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_goteo.py
# ==============================================================================

﻿from .riego_strategy import RiegoStrategy
class RiegoGoteo(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 0.8)  # 20% ahorro


# ==============================================================================
# ARCHIVO 31/37: riego_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_strategy.py
# ==============================================================================

﻿from abc import ABC, abstractmethod

class RiegoStrategy(ABC):
    @abstractmethod
    def regar(self, litros_disponibles: float, consumo_por_cultivo: float) -> float:
        """Devuelve litros restantes tras regar un cultivo."""
        ...

# Esto lo hice para poder cambiar el tipo de riego (goteo o aspersión) cuando quiera.



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 32/37: __init__.py
# Directorio: riego
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\riego\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 33/37: sensor.py
# Directorio: riego
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\riego\sensor.py
# ==============================================================================

﻿from ..patrones.observer.observer import Subject

class SensorTemperatura(Subject):
    def __init__(self):
        super().__init__()
    def nueva_medicion(self, temp_c: float):
        self.notificar(("temp", temp_c))

class SensorHumedad(Subject):
    def __init__(self):
        super().__init__()
    def nueva_medicion(self, humedad_pct: float):
        self.notificar(("hum", humedad_pct))

class RiegoObserver:
    """Adaptador simple para pasar mediciones al RiegoService."""
    def __init__(self, riego_service):
        self.riego_service = riego_service
    def update(self, dato):
        tipo, valor = dato
        if tipo == "temp":
            self.riego_service.set_temp(valor)
        elif tipo == "hum":
            self.riego_service.set_hum(valor)

# Los sensores avisan al riego cuando cambia la temperatura o la humedad.



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 34/37: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\__init__.py
# ==============================================================================

﻿


# ==============================================================================
# ARCHIVO 35/37: mensajes_service.py
# Directorio: servicios
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\mensajes_service.py
# ==============================================================================

﻿class MensajesService:
    def info(self, msg: str): print(f"[INFO] {msg}")
    def warn(self, msg: str): print(f"[WARN] {msg}")
    def error(self, msg: str): print(f"[ERROR] {msg}")


# ==============================================================================
# ARCHIVO 36/37: plantacion_service.py
# Directorio: servicios
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\plantacion_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 37/37: riego_service.py
# Directorio: servicios
# Ruta completa: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\servicios\riego_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 37
# Generado: 2025-10-22 10:52:25
################################################################################

# ==============================================================================
# MAIN DE DEMOSTRACIÓN - agregado manualmente
# ==============================================================================

def main():
    msg = MensajesService()

    # 1) Terreno y plantación
    terreno = Terreno("Lote A", 1000)
    plantacion = Plantacion(terreno, 800)
    ps = PlantacionService(plantacion)
    ps.alta_cultivo("pino", "Pino Paraná", 5.0)
    ps.alta_cultivo("olivo", "Olivo Arbequina", 4.0)
    ps.alta_cultivo("lechuga", "Lechuga Mantecosa", 2.0)

    # 2) Config (Singleton)
    cfg = Config()
    msg.info(f"Tanque inicial: {cfg.tanque_agua_litros}L")

    # 3) Strategy de riego
    riego = RiegoService(RiegoGoteo())

    # 4) Sensores (Observer)
    st = SensorTemperatura()
    sh = SensorHumedad()
    obs = RiegoObserver(riego)
    st.suscribir(obs)
    sh.suscribir(obs)

    # Llegan mediciones
    st.nueva_medicion(12)   # dentro del rango [8..15]
    sh.nueva_medicion(40)   # humedad < 50 => habilita riego

    if riego.condiciones_habilitadas():
        for c in plantacion.cultivos:
            cfg.tanque_agua_litros = riego.regar_cultivo(c.consumo_agua_litros)
            msg.info(f"Se riega {c}. Tanque ahora: {cfg.tanque_agua_litros:.1f}L")
    else:
        msg.warn("Condiciones no habilitadas para riego")

if __name__ == "__main__" and False:
    main()
