from machine import Pin, Timer
from utime import sleep


class OnboardLed(object):
    pin = Pin("LED", Pin.OUT)
    tim = Timer()

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
        return "Stopping blinking onboard LED"


led = OnboardLed()
