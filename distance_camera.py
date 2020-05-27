# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04
# https://gpiozero.readthedocs.io/en/stable/api_output.html#tonalbuzzer

from gpiozero import DistanceSensor, TonalBuzzer
from picamera import PiCamera
from datetime import datetime
from time import sleep

sensor = DistanceSensor(17,4, max_distance=10) #(echo,trigger)
camera = PiCamera()
buzzer = TonalBuzzer(19)

def buzzer_alert():
    notes = ['A5','A3','A5','A3','A5']
    for note in notes:
        buzzer.play(note)
        sleep(0.5)
    buzzer.stop()
    
def take_photo():
    output_folder_path = ""
    timestamp = datetime.now()#.isoformat()
    camera.capture(f"/home/pi/Documents/reference_code/picamera_captures/{timestamp}.jpg")

while True:
    print(sensor.distance)
    if sensor.distance < 1:
        print("Object is close, taking photo now")
        buzzer_alert()
        take_photo()
        sleep(5)
    else:
        sleep(1)
    

