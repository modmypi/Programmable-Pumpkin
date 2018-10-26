from pumpkinpi import PumpkinPi
from time import sleep

# Define a function to control our Pumpkin which takes a PumpkinPi as an argument.
# This script contains flashing LEDs, please take care if you are sensitive to flashing lights.
def pump_pulse(pumpkin):
    pumpkin.sides.left.bottom.pulse(5, 0.5, 1) # Fade in for 5 seconds, fade out for .5 seconds and do this once.
    pumpkin.sides.right.bottom.pulse(5, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.midbottom.pulse(4.5, 0.5, 1)
    pumpkin.sides.right.midbottom.pulse(4.5, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.middle.pulse(4, 0.5, 1)
    pumpkin.sides.right.middle.pulse(4, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.midtop.pulse(3.5, 0.5, 1)
    pumpkin.sides.right.midtop.pulse(3.5, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.top.pulse(3, 0.5, 1)
    pumpkin.sides.right.top.pulse(3, 0.5, 1)
    sleep(.5)
    pumpkin.eyes.blink(.1, .1, 0, 0, 12) # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.
    sleep(3)
    pumpkin.off()

pumpkin = PumpkinPi(pwm=True)

while True:
    pump_pulse(pumpkin)
else:
    pumpkin.close()
