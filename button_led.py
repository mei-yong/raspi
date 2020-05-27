# https://gpiozero.readthedocs.io/en/stable/

from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(18) #GPIO18 - pin#12
button = Button(2) #GPIO2 - pin#3

# while True:
#     led.on()
#     sleep(1)
#     led.off()
#     sleep(1)

# led.source = button

def led_on():
    led.on()
    sleep(1)
    led.off()

button.when_pressed = led_on

pause()

