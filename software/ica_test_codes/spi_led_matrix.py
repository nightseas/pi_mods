# spi_led_matrix.py
# 8x8 LED matrix display demo, which reuses the MAX7219 driver of segment LED on ICA HAT.

import wiringpi2 as wpi
import time

# Import font lib: English 8x8
import font_en_8x8

# CS# of MAX7219
SPI_CS_Pin = 10

# Initialize MAX7219
def max7219Init():
    max7219WriteReg(0x09, 0x00)
    max7219WriteReg(0x0a, 0x03)
    max7219WriteReg(0x0b, 0x07)
    max7219WriteReg(0x0c, 0x01)
    max7219WriteReg(0x0f, 0x00)

# Wirte MAX7219 register
def max7219WriteReg(addr, data):
    io.digitalWrite(SPI_CS_Pin, io.LOW)
    wpi.wiringPiSPIDataRW(0, chr(addr) + chr(data))
    io.digitalWrite(SPI_CS_Pin, io.HIGH)

# Display raw data of font lib on MAX7219
def max7219DiplayMxRaw(index):
    for i in range(1, 9):
        max7219WriteReg(i, font_en_8x8.data[index][i-1])

# Display char of font lib on MAX7219
def max7219DiplayMxChar(char):
    for i in range(1, 9):
        max7219WriteReg(i, font_en_8x8.data[ord(char)-32][i-1])

# Init GPIO to wiringPi pin mode
io = wpi.GPIO(wpi.GPIO.WPI_MODE_PINS)
# Init CS#
io.pinMode(SPI_CS_Pin, io.OUTPUT)
io.digitalWrite(SPI_CS_Pin, io.HIGH)
time.sleep(0.2)

# Init SPI0 for MAX7219
spi = wpi.wiringPiSPISetup(0, 1000000)
if spi<0:
    print("SPI init error!")
    exit(1)
print("SPI init OK!")

# Init MAX7219
max7219Init()
print("MAX7219 init OK!")

# Display font lib
print("Starting display...")
while True:
    for i in range(0, 95):
#        print(i)
        max7219DiplayMxRaw(i)        
        time.sleep(0.1)
#        max7219DiplayMxRaw(0)        
#        time.sleep(0.5)

