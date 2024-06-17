# implementacion del sensor DHT11 para IOT


##para mas informacion sobre 
libreria adafuit_python_dht consulte el [siguiente link:](https://github.com/adafruit/Adafruit_Python_DHT)

sensor [dht11:](https://www.alldatasheet.com/view.jsp?Searchword=Dht11%20datasheet&gad_source=1&gclid=CjwKCAjwmrqzBhAoEiwAXVpgojp5Vp6yo0IFtm0FPFs7tyRPi5oX6oOgAE2ORmjbMNgyObRlEE0zbRoCAzYQAvD_BwE)

## instalacion en ubuntu paso a paso

actualice su sistema
```
sudo apt update && sudo apt upgrade
```

use python3.12
```
sudo apt install python3.12
sudo apt install python3.12-venv
sudo apt install libcairo2-dev pkg-config python3.12-dev
```

instalar pip 
```
sudo apt-get install python3-pip
```

crear entorno virtual
```
python3.12 -m venv venv
```

activar entorno virtual
```
source ./venv/bin/activate
```

instalar adafuit
```
pip install --upgrade pip setuptools wheel
pip install Adafruit_DHT
```

## instalacion rapida 
```
pip  install requirements.txt
```
