# ica_led_seg_spi1.py
# Use AUX SPI(SPI1) to control segment LED on ICA HAT.

#!/usr/bin/env python

import pigpio, time

# Import font lib: English 7-bit Segment
import font_en_seg7

# Soft CS# of MAX7219
SPI_CS_PIN = 26
BUZ_PIN = 4
LED_PIN = [27, 23, 22, 24]


# Using SPI1
AUX_SPI=(1<<8)

# Initialize MAX7219
def max7219Init():
    max7219WriteReg(0x09, 0x00)
    max7219WriteReg(0x0A, 0x03)
    max7219WriteReg(0x0B, 0x07)
    max7219WriteReg(0x0C, 0x01)
    max7219WriteReg(0x0F, 0x00)
    max7219DisplayClear()

# Wirte MAX7219 register
def max7219WriteReg(addr, data):
    pi.write(SPI_CS_PIN, pigpio.LOW)
    #print("[ICA] <max7219WriteReg> addr = 0x%02X, data = 0x%02X" %(addr, data))
    pi.spi_xfer(spi1, [addr & 0xFF, data & 0xFF])
    pi.write(SPI_CS_PIN, pigpio.HIGH)

# Display char of font lib on MAX7219
def max7219DiplayChar(digit, char, dp):
    if not char in font_en_seg7.data.keys():
        print("[ICA] <max7219Diplaychar> Error: Char (%d) can't be displayed!" %ord(char))
        return -1;
    
    if dp != 0:
        max7219WriteReg(digit + 1, font_en_seg7.data[char] + (1<<font_en_seg7.segDP))
    else:
        max7219WriteReg(digit + 1, font_en_seg7.data[char])
    return 0

def max7219DiplayString(string):
    index = 0
    for digit in range(0, 8):
        if index > (len(string) - 1):
            char = " "
        else:
            char = string[index]
                       
        if (index + 1 <= (len(string) - 1)) and (string[index + 1] == "."):
            dp = 1
            index = index + 2
        else:
            dp = 0
            index = index + 1
        max7219DiplayChar(digit, char, dp)

def max7219DisplayClear():
    for dig in range(1, 9):
        max7219WriteReg(dig, 0x00)  


##########################################
#             Main Process               #
##########################################
pi = pigpio.pi() # Connect to local Pi.

# Init Software CS# of MAX7219
pi.set_mode(SPI_CS_PIN, pigpio.OUTPUT)
pi.write(SPI_CS_PIN, pigpio.HIGH)

# Get handle to aux SPI channel 1.
spi1 = pi.spi_open(1, 8000000, AUX_SPI)
if spi1<0:
    print("[ICA] SPI1 init error!")
    exit(1)
else:
    print("[ICA] SPI1 init OK!")

# Init MAX7219 Seg LED driver
max7219Init()
print("[ICA] MAX7219 init OK!")

# Display all the characters symbol lib
print("[ICA] Starting display symbol lib...")
strAz = "0123456789abcdefghijklmnopqrstuvwxyz-."
strDisp = "        "

for char in strAz:
    strDisp = strDisp[1:] + char
    max7219DiplayString(strDisp)
    time.sleep(1)

# Clear resources after display
max7219DisplayClear()
pi.spi_close(spi1)
pi.stop()

