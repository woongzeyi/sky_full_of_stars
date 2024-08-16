from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

p = Pin(0, Pin.OUT)
n = NeoPixel(p, 1)

def percentage_to_rgb(percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100.")
    
    # Convert percentage to a value between 0 and 1
    ratio = percentage / 100.0
    
    # Red to violet spectrum (approximate)
    if ratio <= 0.16:
        # Red to Yellow
        r = 255
        g = int(255 * (ratio / 0.16))
        b = 0
    elif ratio <= 0.33:
        # Yellow to Green
        r = int(255 * (1 - (ratio - 0.16) / 0.17))
        g = 255
        b = 0
    elif ratio <= 0.5:
        # Green to Cyan
        r = 0
        g = 255
        b = int(255 * ((ratio - 0.33) / 0.17))
    elif ratio <= 0.66:
        # Cyan to Blue
        r = 0
        g = int(255 * (1 - (ratio - 0.5) / 0.16))
        b = 255
    elif ratio <= 0.83:
        # Blue to Magenta
        r = int(255 * ((ratio - 0.66) / 0.17))
        g = 0
        b = 255
    else:
        # Magenta to Violet (Purple)
        r = 255
        g = 0
        b = int(255 * (1 - (ratio - 0.83) / 0.17))
    
    return (g, r, b)

while True:
    for i in range(101):
        n.fill(percentage_to_rgb(i))
        n.write()
        sleep_ms(10)