"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/3: plantacion.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: terreno.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\terrenos\terreno.py
# ================================================================================

﻿class Terreno:
    def __init__(self, nombre: str, superficie_m2: float):
        self.nombre = nombre
        self.superficie_m2 = superficie_m2


