from machine import Pin
import time
import math
from neopixel import Neopixel


def mapPixel(x, y):
    if y % 2 == 1:
        return xres * y + x
    else:
        return xres * y + xres - 1 - x


xres = 16
yres = 16
led = Pin(25, Pin.OUT) #25
strip = Neopixel(num_leds=(xres*yres), state_machine=0, pin=28, mode="RGB", delay=0.0001)

led.value(1)
import os
for item in os.listdir():
    try:
        print(item, os.listdir(item))
    except Exception as e:
        print("Skip", item)

numpix = 60

# strip = Neopixel(numpix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
# colors = colors_rgbw


step = round(numpix / len(colors))
current_pixel = 0
strip.brightness(50)

for color1, color2 in zip(colors, colors[1:]):
    strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
    current_pixel += step

strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)

i=0

while True:
    strip.rotate_right(1)
    time.sleep(0.042)
    strip.show()
    i+=1
    print(i, end="\r")
    if i > 100:
        strip.fill((0,0,0))
        strip.show()
        break


led.value(0)

mat = [[0.0,0.2823529541492462,0.08627451211214066,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.0,0.2823529541492462,0.08627451211214066,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [1.0,1.0,1.0,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [1.0,1.0,1.0,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [1.0,1.0,1.0,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [1.0,1.0,1.0,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.9529411792755127,0.6823529601097107,0.7254902124404907,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6784313917160034,0.01568627543747425,0.11764705926179886,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.35686275362968445,0.0,0.054901961237192154,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.6901960968971252,0.9254902005195618,0.9529411792755127,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],
        [0.2980392277240753,0.15294118225574493,0.03529411926865578,],]

for i in range((xres*yres)):
    strip.set_pixel(i, mat[i]*255, 255)

strip.show()
time.sleep(1)

strip.fill((0,0,0))
strip.show()