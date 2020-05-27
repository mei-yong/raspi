# https://gpiozero.readthedocs.io/en/stable/

from gpiozero import LED
from time import sleep

led = LED(18)
# corresponds with GPIO18
# aka pin#12
# aka 6th from the top right of the board

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
