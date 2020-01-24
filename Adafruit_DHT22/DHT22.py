import Adafruit_DHT
from time import strftime, sleep

sensor = Adafruit_DHT.DHT22
f_name = "/home/pi/fin_code/data_store/Jan20_2020_dht.txt"
pin = 27

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #print("test_1, %s, %s",humidity,temperature)
    if humidity is not None and temperature is not None:
        f_temperature = temperature * (9/5) +32
        with open(f_name, "a") as fid:
            fid.write("{} ,{}C , {}F ,{}%\n".format(strftime('%H:%M:%S'),
                                          round(temperature, 1), round(f_temperature, 1), round(humidity, 1)))
    else:
        1
    sleep(30)
