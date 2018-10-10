from gpiozero import LEDBoard

class PumpkinPi(LEDBoard):
    # Set up a PumpkinPi using GPIO Zero to build a class.
    # To use:
    # pumpkin = PumpkinPi() for a simple instance using LED class.
    # pumpkin = PumpkinPi(pwm=True) for a version which can use PWM.
    # See example files in this repo for more examples of use...
    def __init__(self, pwm=False, initial_value=False, pin_factory=None):
        super(PumpkinPi,self).__init__(
            sides=LEDBoard(
                left=LEDBoard(
                    bottom=18, midbottom=17, middle=16, midtop=13, top=24,
                    pwm=pwm, initial_value=initial_value,
                    _order=('bottom','midbottom','middle','midtop','top'),
                    pin_factory=pin_factory),
                right=LEDBoard(
                    bottom=19, midbottom=20, middle=21, midtop=22, top=23,
                    pwm=pwm, initial_value=initial_value,
                    _order=('bottom','midbottom','middle','midtop','top'),
                    pin_factory=pin_factory),
                pwm=pwm, initial_value=initial_value,
                _order=('left','right'),
                pin_factory=pin_factory
                ),
            eyes=LEDBoard(
                left=12, right=6,
                pwm=pwm, initial_value=initial_value,
                _order=('left','right'),
                pin_factory=pin_factory
                ),
            pwm=pwm, initial_value=initial_value,
            _order=('eyes','sides'),
            pin_factory=pin_factory
        )
