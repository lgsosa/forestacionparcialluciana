"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\riego
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\riego\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/2: sensor.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\riego\sensor.py
# ================================================================================

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


