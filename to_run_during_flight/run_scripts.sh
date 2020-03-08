#!/bin/bash
gpspipe -r -d -l -o /home/pi/to_run_during_flight/berry_GPS_data/`date +"%Y%m%d-%H-%M-%S"`.nmea
#echo "done!!!"
python3 ~/to_run_during_flight/Adafruit_DHT22/DHT22.py &
python3 ~/to_run_during_flight/pi-cam-test-filter/pi_cam_filter.py &
python3 ~/to_run_during_flight/python-BMP280-temperature-pressure/bmp280.py &