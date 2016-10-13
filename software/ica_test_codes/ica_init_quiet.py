# ica_init_quiet.py
# This script implements a quiet initailization of ICA HAT.
# Turn off buzzer and LEDs, and set CS# pin of MAX7219.

#!/usr/bin/env python

import pigpio, time
import netifaces as ni


# Import font lib: English 8x8
import font_en_seg7

# Soft CS# of MAX7219
SPI_CS_PIN = 26
BUZ_PIN = 4
LED_PIN = [27, 23, 22, 24]

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
    pi.write(LED_PIN[i], pigpio.HIGH)

# Init Buzzer
pi.set_mode(BUZ_PIN, pigpio.OUTPUT)
pi.write(BUZ_PIN, pigpio.LOW)
pi.stop()

