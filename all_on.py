from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (11,16,17,18,19,20,21,22,23,24,12)

GPIO.setup(LEDS, GPIO.OUT, initial=1)

try:
    while True:
	    sleep(.5)
except:
    GPIO.cleanup()