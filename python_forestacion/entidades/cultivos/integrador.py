"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/6: cultivo.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: lechuga.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

﻿from .cultivo import Cultivo
class Lechuga(Cultivo):
    def tipo(self) -> str: return "Lechuga"


# ================================================================================
# ARCHIVO 4/6: olivo.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

﻿from .cultivo import Cultivo
class Olivo(Cultivo):
    def tipo(self) -> str: return "Olivo"


# ================================================================================
# ARCHIVO 5/6: pino.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

﻿from .cultivo import Cultivo
class Pino(Cultivo):
    def tipo(self) -> str: return "Pino"


# ================================================================================
# ARCHIVO 6/6: zanahoria.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

﻿from .cultivo import Cultivo
class Zanahoria(Cultivo):
    def tipo(self) -> str: return "Zanahoria"


