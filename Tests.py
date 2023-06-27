# - - - - - - - IMPORTS - - - - - - -
import png
import uos
import utime

from machine import Pin, SPI
from neopixel import Neopixel
from Dependancies.sdcard import SDCard

# - - - - - - - FINALS - - - - - - -
BOARD_LED_NUM = 16*16
BOARD_LED_PIN = 28
BOARD = Neopixel(num_leds=(BOARD_LED_NUM), 
                state_machine=0, 
                pin=BOARD_LED_PIN, 
                mode="RGB", 
                delay=0.0001
            )
LED = Pin('LED', Pin.OUT)

SD_CLK = 2
SD_3V3 = 3
SD_MOSI = 5
SD_MISO = 6
SD_CS = 7
SD_GND = 40


# - - - - - - - SETUP - - - - - - -
BOARD.brightness(255)

# - - - - - - - METHODS - - - - - - -
def clear():
    LED.value(0)
    BOARD.fill((0,0,0))
    BOARD.show()


# - - - - - - - MAIN - - - - - - -
def main():
	# on-board LED start up test
    LED.value(1)
    print("Program Started!")
    utime.sleep(1)
    LED.toggle()

    # LED Board start up test
    c = tuple([100, 150, 200])
    BOARD.fill(c)
    BOARD.show()
    utime.sleep(1)

    # image test
    img_src = "Dependancies/apple.png"
    png_reader=png.Reader(img_src).asRGB()
    print(png_reader[0])
    

    clear()
    print("Goodbye!")

# - - - - - - - RUN - - - - - - -
if __name__ == "__main__":
	main()
