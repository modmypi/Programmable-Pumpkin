from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (11,16,17,18,19,20,21,22,23,24,12)

GPIO.setup(LEDS, GPIO.OUT, initial=0)

try:
	i = 0
	led_length = len(LEDS)
	while i < led_length:
		if i == 0:
			GPIO.output(LEDS[led_length-1],0)
		else:
			GPIO.output(LEDS[i-1],0)
		GPIO.output(LEDS[i],1)
		i += 1
		if i == led_length:
			i = 0
		sleep(.2)
except:
	GPIO.cleanup()