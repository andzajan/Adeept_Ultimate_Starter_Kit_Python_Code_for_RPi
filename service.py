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
import os

LedPin = [11, 13, 15, 29, 31, 33, 35, 37]    # pin11
count = 0
length = [0.1, 0.2, 0.5, 1]
lnum = [1,2,3,4]

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location

GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.LOW) # Set pin to high(+3.3V) to off the led
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		new_lnum = random.sample (lnum,1)[0]
		#print new_lnum
		new_pin = random.sample (LedPin, new_lnum)
		new_length = random.sample (length, 1)[0]
		#print new_length
		#print '...led on'
		GPIO.output(new_pin, GPIO.HIGH)  # led on
		time.sleep(new_length)
		#print 'led off...'
		GPIO.output(new_pin, GPIO.LOW) # led off
		time.sleep(new_length)
		count = count + 1

		if GPIO.input(10) == GPIO.HIGH:
        		print("Button was pushed!")
			GPIO.output (LedPin, GPIO.LOW)
			GPIO.cleanup()
			os.system ("shutdown -h now")
except KeyboardInterrupt:
#except if GPIO.input(10) == GPIO.HIGH:
	GPIO.cleanup()
	print "\n Blink cycles:", count
