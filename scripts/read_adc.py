from machine import Pin, ADC

adc0 = ADC(0)

def val():
    value = adc0.read_u16() / (2**16)
    return f"{value:.2%}"