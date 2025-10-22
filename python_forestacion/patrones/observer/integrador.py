"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\observer
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\observer\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/2: observer.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\patrones\observer\observer.py
# ================================================================================

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


