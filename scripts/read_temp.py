from machine import ADC, Timer


class TempSensor(object):
    sensor = ADC(4)
    tim = Timer()

    conversion_factor = 3.3 / (65535)

    def read_u16(self, timer):
        """Read temperature from sensor, return as float in degrees C."""
        
        reading = self.sensor.read_u16() * self.conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        print(f"{temperature:.2f} C")

    def start_temp_reading(self):
        self.tim.init(freq=1, mode=Timer.PERIODIC, callback=self.read_u16)
