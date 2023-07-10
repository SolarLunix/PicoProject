# - - - - - - - IMPORTS - - - - - - -
import os
import utime

from machine import Pin, SPI
from neopixel import Neopixel
# from sdcard import SDCard

# - - - - - - - FINALS - - - - - - -
BOARD_LED_NUM = 16*16
BOARD_LED_PIN = 28
BOARD = Neopixel(num_leds=(BOARD_LED_NUM), 
                state_machine=0, 
                pin=BOARD_LED_PIN, 
                delay=0.0001
            )
LED = Pin('LED', Pin.OUT)

#SD_CLK = Pin(2)
#SD_MOSI = Pin(3)
#SD_MISO = Pin(4)
#SD_CS = Pin(5)
# SD_GND = Pin(40)


# - - - - - - - SETUP - - - - - - -
BOARD.brightness(255)

# - - - - - - - METHODS - - - - - - -
def clear():
    LED.value(0)
    BOARD.fill((0, 0, 0), 0)
    BOARD.show()

def read_img(img_path):
    raw_img = []
    with open(img_path) as img_file:
        for line in img_file.readlines():
            vals = (line.replace("\n", "")).split(",")
            pixel = []
            for v in vals:
                pixel.append(int(v))
            raw_img.append(pixel)

    img = [[0 for x in range(4)] for y in range(BOARD_LED_NUM)] 
    for i, pixel in enumerate(raw_img):
        y = int(i%16)
        x = int((i-y)/16)
        if x%2 == 1:
            place = (x * 16) + y
        else:
            place = int((x * 16) + (15 - y))
        img[place] = pixel
    return img

def display(img):
    for i, pixel in enumerate(img):
        r, g, b, a = pixel
        BOARD.set_pixel(i, (g, r, b), a)
    BOARD.show()

# - - - - - - - MAIN - - - - - - -
def main():
	# on-board LED start up test
    LED.value(1)
    print("Program Started!")
    utime.sleep(1)
    LED.toggle()
    # Clear in case error
    clear()

    # LED Matrix test
    BOARD.fill((255, 0, 0), 255)
    BOARD.show()
    utime.sleep(1)
    clear()

    BOARD.fill((0, 255, 0), 255)
    BOARD.show()
    utime.sleep(1)
    clear()

    BOARD.fill((0, 0, 255), 255)
    BOARD.show()
    utime.sleep(1)
    clear()

    display(read_img("/Dependancies/imgs/welcome2.csv"))
    utime.sleep(1)
    clear()

    display(read_img("/Dependancies/imgs/welcome.csv"))
    utime.sleep(10)
    clear()

    print("Goodbye!")

# - - - - - - - RUN - - - - - - -
if __name__ == "__main__":
	main()
