from picamera import PiCamera
from time import sleep

camera = PiCamera()

"camera.resolution = (3280, 2464)"
camera.resolution = camera.MAX_RESOLUTION
"camera.framerate = 15"
i = 0
while True:
    sleep(5)
    camera.capture('/home/pi/pi_image/Still_Image/test%s.jpg' % i)
    camera.capture(format='jpeg', bayer=True, output='/home/pi/pi_image/Raw_Image/test%s.jpg' % i)
    i = i + 1
