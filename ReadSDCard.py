from machine import Pin
from neopixel import Neopixel
import os
import time
import machine
from Dependancies.sdcard import SDCard
import uos

pin = Pin("LED", Pin.OUT)

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(9, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(8))

# Initialize SD card
sd = SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

#os.mount(machine.SDCard(), "/sd")

xres = 16
yres = 16

strip = Neopixel(num_leds=(xres*yres), state_machine=0, pin=28, mode="RGB", delay=0.0001)


files = os.listdir("/sd")

if len(files) > 0:
    for f in files:
        strip.fill((50,50,50))
        strip.show()
        time.sleep(.5)
        strip.fill((0,0,0))
        strip.show()
        time.sleep(.5)
        print(f)
else: 
    pin.value(1)
    time.sleep(0.1)
    pin.value(0)
    time.sleep(0.5)
    pin.value(1)
    time.sleep(0.1)
    pin.value(0)
    time.sleep(0.5)
    pin.value(1)
    time.sleep(0.1)
    pin.value(0)
    time.sleep(0.5)
