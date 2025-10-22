from ...entidades.cultivos.pino import Pino
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
