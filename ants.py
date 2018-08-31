#!/usr/bin/python

#LED1 - 18 - 24
#LED2 - 16 - 23
#LED3 - 15 - 22
#LED4 - 40 - 21
#LED5 - 38 - 20
#LED6 - 35 - 19
#LED7 - 12 - 18
#LED8 - 11 - 17
#LED9 - 36 - 16
#LED10 - 33 - 13
#LED11 (GREEN) - 31 - 6
#LED12 (GREEN) - 32 - 12

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (18,17,16,13,12,24,23,6,22,21,20,19)

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
