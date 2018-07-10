#!/usr/bin/python3

import gpiozero as GPIO
import time

inpin = GPIO.InputDevice(4,pull_up=False)
outpin = GPIO.OutputDevice(17,active_high=True,initial_value = False)

print('Input initially measures: '+str(inpin.is_active))

print('Turning on the Output...')
outpin.on()

print('Input now measures: '+str(inpin.is_active))
