class _Config:
    def __init__(self):
        self.tanque_agua_litros = 100  # stock inicial

class Config:
    _inst = None
    def __new__(cls):
        if cls._inst is None:
            cls._inst = _Config()
        return cls._inst

# Uso una sola instancia para el tanque de agua así no se mezclan los valores.
