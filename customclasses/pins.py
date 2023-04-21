from machine import Pin, Timer, PWM

class OutputPin(object):
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)
        self.tim = Timer()
        self.mode = 'binary'


    def toggle(self, timer):
        self.pin.toggle()

    def off(self):
        self.pin.off()
        return "Turning off onboard LED"

    def on(self):
        self.pin.on()
        return "Turning on onboard LED"

    def start_blinking(self, period=1000):
        self.tim.init(mode=Timer.PERIODIC, period=period, callback=self.toggle)
        return "Starting blinking onboard LED"
    
    def stop_blinking(self):
        self.tim.deinit()
        self.pin.off()


class BreathingPin(object):
    def __init__(self, pin):
        self.pin = PWM(Pin(pin))
        self.pin.freq(1000)
        self.pin.duty_u16(0)
        self.value = 0

    def breathe(self, timer):
        self.value += self.speed
        
        self.pin.duty_u16(int(self.value * 500))
        if self.value >= 100:
            self.value = 100
            self.speed = -5
        elif self.value <= 0:
            self.value = 0
            self.speed = 5
    
    def start_breathing(self, speed=5, value=0):
        self.speed = speed
        self.value = value
        self.tim = Timer()
        self.tim.init(period=100, callback=self.breathe)
    
    def stop_breathing(self):
        self.value = 0
        self.pin.duty_u16(0)
        self.tim.deinit()

    def set_percentage(self, percentage):
        if percentage < 0 or percentage > 100:
            return 'Percentage must be between 0 and 100'
        if hasattr(self, 'tim'):
            self.tim.deinit()
        newvalue = int(percentage / 100 * 2**16)
        self.pin.duty_u16(newvalue)
        self.value = percentage
        
        
