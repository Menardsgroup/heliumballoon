from picamera import PiCamera
from time import sleep

camera = PiCamera()

"camera.resolution = (3280, 2464)"
camera.resolution = camera.MAX_RESOLUTION
"camera.framerate = 15"
i = 0

while True:
    sleep(10)
    camera.capture('/home/pi/to_run_during_flight/pi-cam-test-filter/StillImage_nofilter/test%s.jpg' % i)
    camera.capture(format='jpeg', bayer=True, output='/home/pi/to_run_during_flight/pi-cam-test-filter/Raw_Image_nofilter/test%s.jpg' % i)
    i = i + 1
    print("camera works!")
