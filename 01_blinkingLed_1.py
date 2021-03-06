#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 01_blinkingLed_1.py
# Description : make an led blinking.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time
import random

LedPin = [11, 13, 15]    # pin11
count = 0
length = [0.1, 0.2, 0.5, 1]

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location

GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.LOW) # Set pin to high(+3.3V) to off the led

try:
	while True:
		new_pin = random.sample (LedPin, 2)
		new_length = random.sample (length, 1)[0]
		print new_length
		print '...led on'
		GPIO.output(new_pin, GPIO.HIGH)  # led on
		time.sleep(new_length)
		print 'led off...'
		GPIO.output(new_pin, GPIO.LOW) # led off
		time.sleep(new_length)
		count = count + 1
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
	#GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource
	print "\n Blink cycles:", count
