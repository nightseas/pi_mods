# ica_ip_disp.py
# Display IP address of Ethernet port, which could help user to
# find out the IP on start up when Pi acts as a headless server.

#!/usr/bin/env python

import pigpio, time
import netifaces as ni


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

# Init LEDs
for i in range(0, len(LED_PIN)):
    pi.set_mode(LED_PIN[i], pigpio.OUTPUT)
    pi.write(LED_PIN[i], pigpio.LOW)

# Init Buzzer
pi.set_mode(BUZ_PIN, pigpio.OUTPUT)
pi.write(BUZ_PIN, pigpio.HIGH)
time.sleep(0.1)
pi.write(BUZ_PIN, pigpio.LOW)

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

# Get local IP addr
ni.ifaddresses('eth0')
strIP = ni.ifaddresses('eth0')[2][0]['addr']
print ("[ICA] Local IP addr is %s" %strIP)
localIP = strIP.split('.')

# Second beep after display system init
pi.write(BUZ_PIN, pigpio.HIGH)
time.sleep(0.1)
pi.write(BUZ_PIN, pigpio.LOW)

# Turn off all LEDs after display system init
for i in range(0, len(LED_PIN)):
    pi.write(LED_PIN[i], pigpio.HIGH)

# Dislpay IP addr
print("[ICA] Starting display IP addr...")
for i in range(0, 10):
    max7219DiplayString(" ip addr")
    time.sleep(3)
    max7219DiplayString("%4d.%4d."%(int(localIP[0]), int(localIP[1])))
    time.sleep(3)
    max7219DiplayString("%4d.%4d"%(int(localIP[2]), int(localIP[3])))
    time.sleep(3)

# Thrid beep after display done
pi.write(BUZ_PIN, pigpio.HIGH)
time.sleep(0.1)
pi.write(BUZ_PIN, pigpio.LOW)

# Clear resources after display
max7219DisplayClear()
pi.spi_close(spi1)
pi.stop()

