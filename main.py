from python_forestacion.entidades.terrenos.terreno import Terreno
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.plantacion_service import PlantacionService
from python_forestacion.servicios.riego_service import RiegoService
from python_forestacion.patrones.strategy.riego_goteo import RiegoGoteo
from python_forestacion.patrones.singleton.config import Config
from python_forestacion.riego.sensor import SensorTemperatura, SensorHumedad, RiegoObserver
from python_forestacion.servicios.mensajes_service import MensajesService

# Acá lo probé con varios cultivos para ver si bajaba bien el tanque

def main():
    msg = MensajesService()

    # 1) Terreno y plantación
    terreno = Terreno("Lote A", 1000)
    plantacion = Plantacion(terreno, 800)
    ps = PlantacionService(plantacion)
    ps.alta_cultivo("pino", "Pino Paraná", 5.0)
    ps.alta_cultivo("olivo", "Olivo Arbequina", 4.0)
    ps.alta_cultivo("lechuga", "Lechuga Mantecosa", 2.0)

    # 2) Config (Singleton)
    cfg = Config()
    msg.info(f"Tanque inicial: {cfg.tanque_agua_litros}L")

    # 3) Strategy de riego
    riego = RiegoService(RiegoGoteo())

    # 4) Sensores (Observer)
    st = SensorTemperatura()
    sh = SensorHumedad()
    obs = RiegoObserver(riego)
    st.suscribir(obs); sh.suscribir(obs)

    # Llegan mediciones
    st.nueva_medicion(12)   # dentro del rango [8..15]
    sh.nueva_medicion(40)   # humedad < 50 => habilita riego

    if riego.condiciones_habilitadas():
        for c in plantacion.cultivos:
            cfg.tanque_agua_litros = riego.regar_cultivo(c.consumo_agua_litros)
            msg.info(f"Se riega {c}. Tanque ahora: {cfg.tanque_agua_litros:.1f}L")
    else:
        msg.warn("Condiciones no habilitadas para riego")

if __name__ == "__main__":
    main()
