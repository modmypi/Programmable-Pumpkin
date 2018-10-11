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

# sudo apt-get install python-gpiozero python3-gpiozero

from pumpkinpi import PumpkinPi
from gpiozero.tools import random_values
from signal import pause

pumpkin = PumpkinPi(pwm=True)
leds = pumpkin.leds

try:
	for led in leds:
		led.source_delay = 0.1
		led.source = random_values()
	pause()
except KeyboardInterrupt:
	pumpkin.off()
	pumpkin.close()
