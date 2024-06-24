import Adafruit_DHT
import time


def get_temp_RH(pin):

    sensor = Adafruit_DHT.DHT11    
    humedad, temperatura = Adafruit_DHT.read(sensor, pin)

    return  {
        temperatura,
        humedad
    }


def start_sensor(pin = 23, sensor_delay = 3):
    interations = True
    while interations:
        try:
            humedad, temperatura = get_temp_RH(pin)
        except ValueError:
            humedad = None
            temperatura = None
            print("error al leer")
        finally:
            print(f'temperatura: {temperatura}°C humedad: {humedad} %')

        time.sleep(sensor_delay)


if __name__ == '__main__':
    
    try:
        start_sensor(23, 5)
    except KeyboardInterrupt:
        print("\n bye")

    