class Subject:
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
