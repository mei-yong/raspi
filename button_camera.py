# https://gpiozero.readthedocs.io/en/stable/

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(2)
camera = PiCamera()

def capture():
    print("Camera was activated")
    timestamp = datetime.now().isoformat()
    camera.capture("/home/pi/Documents/reference_code/picamera_captures/%s.jpg" % timestamp)

button.when_pressed = capture
pause()
    