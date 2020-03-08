import Adafruit_DHT
from time import strftime, sleep

sensor = Adafruit_DHT.DHT22
f_name = "/home/pi/to_run_during_flight/Adafruit_DHT22/Feb21_2020_dht.txt"
pin = 27

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("sensor works!")
    if humidity is not None and temperature is not None:
        f_temperature = temperature * (9/5) +32
        with open(f_name, "a") as fid:
            fid.write("{} ,{}C , {}F ,{}%\n".format(strftime('%H:%M:%S'),
                                          round(temperature, 1), round(f_temperature, 1), round(humidity, 1)))
    else:
        1
    sleep(30)
