# PumpkinPi - Sample Code

Here you will find three different code examples to get you started with the PumpkinPi from ModMyPi.

There is either a [kit you can build](https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/halloween-pumpkin-solder-kit) or a [pre-assembled Pumpkin](https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/halloween-pumpkin-programmable-kit) for you to get your Halloween spook on with.

### all_on.py

As the name of the file implies, this simply turns on all the LEDS on the board.

### ants.py

This script simply turns each led on then off in sequence.

### pumpkinpi.py

The PumpkinPi class. To use include:

```
from pumpkinpi import PumpkinPi

pumpkin = PumpkinPi()
pumpkin.on()
```
This class uses [gpiozero](https://github.com/RPi-Distro/python-gpiozero) and the PumpkinPi board can be set up as either a set of LEDs which can be on or off. Or it can be setup as a PWM style LED board with the following:
```
pumpkin = PumpkinPi(pwm=True)
pumpkin.pulse()
```

### random_leds.py

This script will randomly turn on/off the leds at random brightnesses.

## Download and Run

To download the sample code simply run the following command:

```
git clone https://github.com/modmypi/Programmable-Pumpkin/
```

To run the sample code:

```
cd Programmable-Pumpkin
```

```
sudo python ants.py
```
