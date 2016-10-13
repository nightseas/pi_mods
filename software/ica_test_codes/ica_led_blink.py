# ica_led_blink.py
# Simple test code for LEDs on ICA HAT.

import wiringpi2 as wpi
import time

# Pin definition of LED
LED_PIN = [2, 4, 3, 5]

# Init GPIO to wiringPi pin mode
io = wpi.GPIO(wpi.GPIO.WPI_MODE_PINS)

# Init LED pins
for i in range(0, 4):
    io.pinMode(LED_PIN[i], io.OUTPUT)
    io.digitalWrite(LED_PIN[i], io.HIGH)

# LED Flasher
while True:
    for ledPinOn in range(0, 4):
        for i in range(0, 4):
            io.digitalWrite(LED_PIN[i], io.HIGH)
        io.digitalWrite(LED_PIN[ledPinOn], io.LOW)
        time.sleep(0.3)

