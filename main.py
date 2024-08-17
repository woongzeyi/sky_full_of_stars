from machine import Pin
from neopixel import NeoPixel
import time


TOTAL_LED = 225
LED_EACH_SIDE = 15

PATTERNS = {
    'LOVE': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (28, 237, 36), (28, 237, 36), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
}

MASKS = {
    'LOVE': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'LOVE1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'LOVE2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
}


led = NeoPixel(Pin(0, Pin.OUT), 225)
indicator = Pin(1, Pin.OUT)


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


def led_test(update_time, static_time):
    for i in range(TOTAL_LED):
        led[i] = (255, 0, 0)
        led.write()
        time.sleep_ms(update_time)
    for i in range(TOTAL_LED):
        led[i] = (0, 255, 0)
        led.write()
        time.sleep_ms(update_time)
    for i in range(TOTAL_LED):
        led[i] = (0, 0, 255)
        led.write()
        time.sleep_ms(update_time)
    for i in range(TOTAL_LED):
        led[i] = (255, 255, 255)
        led.write()
        time.sleep_ms(update_time)
    time.sleep_ms(static_time)


def static_image(i):
    for i, j in enumerate(i):
        if j == None:
            continue
        led[i] = j
    led.write()
    
    
def mask_as_static_image(i, color):
    for i, j in enumerate(i):
        led[i] =  color if j else (0, 0, 0)
    led.write()
    

def linear_gradient_in_horizontal_direction():
    pass


def linear_gradient_in_diagonal_direction():
    pass


def ascending_spectrum(update_time):
    for i in range(LED_EACH_SIDE):
        for j in range(TOTAL_LED):
            led[j] = percentage_to_rgb(int((j + i) % LED_EACH_SIDE / LED_EACH_SIDE * 100))
        led.write()
        time.sleep_ms(update_time)
        
        
def masked_ascending_spectrum(mask, update_time):
    for i in range(LED_EACH_SIDE):
        for j in range(TOTAL_LED):
            if mask[j]:
                led[j] = percentage_to_rgb(int((j + i) % LED_EACH_SIDE / LED_EACH_SIDE * 100))
            else :
                led[j] = (0, 0, 0)
        led.write()
        time.sleep_ms(update_time)


def main():
    indicator.on()
    while True:
        mask_as_static_image(MASKS['LOVE'], (0, 255, 0))
        time.sleep_ms(75)
        mask_as_static_image(MASKS['LOVE1'], (0, 255, 0))
        time.sleep_ms(75)
        mask_as_static_image(MASKS['LOVE2'], (0, 255, 0))
        time.sleep_ms(75)
        mask_as_static_image(MASKS['LOVE1'], (0, 255, 0))
        time.sleep_ms(75)
        mask_as_static_image(MASKS['LOVE'], (0, 255, 0))
        time.sleep_ms(75)
        
        
main()
