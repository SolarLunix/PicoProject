from machine import PIN, SDCard
from neopixel import Neopixel
import os
import time


os.mount(SDCard(), "/sd")

xres = 16
yres = 16

strip = Neopixel(num_leds=(xres*yres), state_machine=0, pin=28, mode="RGB", delay=0.0001)


files = os.listdir("/sd")

if len(files) > 0:
    strip.fill((255,0,0))
    strip.show()
    time.sleep(.5)


for f in files:
    strip.fill((255,255,255))
    strip.show()
    time.sleep(.5)
    strip.fill((0,0,0))
    strip.show()
    time.sleep(.5)