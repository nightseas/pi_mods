# ica_key_read.py
# Simple test code for buttons on ICA HAT.

import wiringpi2 as wpi
import time

# Pin definition of Keys
KEY_PIN = [23, 26, 21, 6, 22]
KEY_NAME = ["UP", "CENTER", "DOWN", "LEFT", "RIGHT"]

def ICA_ReadKey(num):
    key = io.digitalRead(KEY_PIN[num])
    if key == io.LOW:
        # Delay for a while and re-detect the key status
        # It's used to filter glitches on the signal
        time.sleep(0.01)
        if key == io.LOW:
            return 1
    return 0
        
    

# Init GPIO to wiringPi pin mode
io = wpi.GPIO(wpi.GPIO.WPI_MODE_PINS)

# Init key pins
for i in range(0, 5):
    io.pinMode(KEY_PIN[i], io.INPUT)

while True:
    for i in range(0, 5):
        if ICA_ReadKey(i) == 1:
            print("Key %s is pressed!" %KEY_NAME[i])
            time.sleep(0.5)

