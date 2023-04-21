from customclasses.pins import BreathingPin

pin_dict = {}
for i in range(5):
    pin_dict[i] = BreathingPin(i)

def stop_all():
    for p in pin_dict.values():
        p.stop_breathing()

def start_all(speed=5):
    for p in pin_dict.values():
        p.start_breathing(speed)

def staggered_start(diff=20, speed=5):
    start_value = 0
    for p in pin_dict.values():
        p.start_breathing(speed = speed, value=start_value)
        start_value += diff
    