from rpi_ws281x import PixelStrip, Color
import time

LEDCOUNT = 10  # Number of LEDs
GPIOPIN = 18   # The Kano Ring uses pin 18 
FREQ = 800000
DMA = 10
INVERT = False
BRIGHTNESS =  255

strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)
strip.begin()

for x in range(0,11):
    strip.setPixelColor(x, Color(0,0,0))
    strip.show()
