"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/4: riego_aspersion.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_aspersion.py
# ================================================================================

﻿from .riego_strategy import RiegoStrategy
class RiegoAspersion(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 1.1)  # 10% extra por perdidas


# ================================================================================
# ARCHIVO 3/4: riego_goteo.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_goteo.py
# ================================================================================

﻿from .riego_strategy import RiegoStrategy
class RiegoGoteo(RiegoStrategy):
    def regar(self, litros_disponibles, consumo_por_cultivo):
        return litros_disponibles - (consumo_por_cultivo * 0.8)  # 20% ahorro


# ================================================================================
# ARCHIVO 4/4: riego_strategy.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\strategy\riego_strategy.py
# ================================================================================

﻿from abc import ABC, abstractmethod

class RiegoStrategy(ABC):
    @abstractmethod
    def regar(self, litros_disponibles: float, consumo_por_cultivo: float) -> float:
        """Devuelve litros restantes tras regar un cultivo."""
        ...

# Esto lo hice para poder cambiar el tipo de riego (goteo o aspersión) cuando quiera.


