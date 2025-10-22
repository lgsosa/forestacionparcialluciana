"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\singleton
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\singleton\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/2: config.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\singleton\config.py
# ================================================================================

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


