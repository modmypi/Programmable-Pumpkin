from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (11,16,17,18,19,20,21,22,23,24,12)
GREEN = (11,17,20,22,24)
RED = (16,18,19,21,23)
WHITE = (12)

GPIO.setup(LEDS, GPIO.OUT, initial=0)
GPIO.output(WHITE,1)

try:
	while True:
		GPIO.output(GREEN,1)
		sleep(.5)
		GPIO.output(GREEN,0)
		GPIO.output(RED,1)
		sleep(.5)
		GPIO.output(RED,0)
except:
	GPIO.cleanup()