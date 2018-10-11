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

from pumpkinpi import PumpkinPi
from time import sleep

pumpkin = PumpkinPi()
leds = pumpkin.leds

step = [2,3,4,5,0,6,11,1,10,9,8,7]

try:
        for index in step:
                leds[index].on()
                sleep(0.2)
                leds[index].off()
except KeyboardInterrupt:
        pumpkin.off()
        pumpkin.close()
