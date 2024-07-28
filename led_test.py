from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms


n = NeoPixel(Pin(8, Pin.OUT), 5)

while True:
    n.fill((10, 0, 0))
    sleep_ms(500)
    n.fill((0, 10, 0))
    sleep_ms(500)