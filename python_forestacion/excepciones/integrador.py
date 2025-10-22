"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones
Fecha: 2025-10-22 10:52:25
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\__init__.py
# ================================================================================

﻿


# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class AguaAgotadaException(ForestacionException):
    pass


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

﻿class ForestacionException(Exception):
    """Excepcion base del dominio."""
    pass


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class MensajesException(ForestacionException):
    pass


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class PersistenciaException(ForestacionException):
    pass


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Users\Luci\OneDrive\Escritorio\Parcial Diseño\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

﻿from .forestacion_exception import ForestacionException
class SuperficieInsuficienteException(ForestacionException):
    pass


