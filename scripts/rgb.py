from customclasses.pins import BreathingPin
from utime import sleep

colors = {
    'red': BreathingPin(0),
    'green': BreathingPin(1),
    'blue': BreathingPin(2)
}

def set_leds(red, green, blue):
    colors['red'].set_percentage(red)
    colors['green'].set_percentage(green)
    colors['blue'].set_percentage(blue)


set_leds(0, 0, 0)

