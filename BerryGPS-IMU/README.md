## BerryGPS and BerryIMU

### BerryGPS Setup Guide with Raspberry Pi
1. Go to http://ozzmaker.com/berrygps-berrygps-imu-quick-start-guide/ and read all the sections
2. For BerryGPS to obtain a fix, make sure it is exposed to clear sky
3. In command line, use cgps (after you set everything up and the light on BerryGPS is blinking!)
4. If interested, use u-center software developed by u-blox. Download the software here (only compatible with Microsoft): 
    https://www.u-blox.com/en/product/u-center
5. Connect the computer to the same wifi network as the Raspberry Pi, then follow instruction guide for u-center setup,
again on ozzmaker.com
6. Make use of data logger, setup guide again on ozzmaker.com. Store data with NMEA files, and upload to https://www.gpsvisualizer.com/

### BerryIMU Setup Guide with Raspberry Pi
1. Go to http://ozzmaker.com/berryimu-quick-start-guide/ and read all sections
2. Once you have git cloned the repository, we will be interested in running bmp280 for getting temperature and pressure data.
