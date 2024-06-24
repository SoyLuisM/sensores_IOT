from src.sensores.get_tem_hum import start_sensor

try:
    start_sensor(23, 3)
except KeyboardInterrupt:
    print("\n bye")

