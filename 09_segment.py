#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#pins = [11,12,13,15,16,18,22,7]
pins = [7,22,18,16,15,13,12,11]

dats = {"0":0x3f,
	"1":0x06,
	"2":0x5b,
	"3":0x4f,
	"4":0x66,
	"5":0x6d,
	"6":0x7d,
	"7":0x07,
	"8":0x7f,
	"9":0x6f,
	"A":0x77,
	"b":0x7c,
	"C":0x39,
	"d":0x5e,
	"E":0x79,
	"F":0x71,
	".":0x80}

for key in dats:
	print key, "corresponds to", bin(dats[key])

def setup():
	GPIO.setmode(GPIO.BOARD)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   # Set pin mode as output
		GPIO.output(pin, GPIO.LOW)

def writeOneByte(val, pins):
	bin_val =str(bin(val))[:2].zfill(8)
	for pin in range(0,8):
		GPIO.output (pins[pin], int(bin_val[pin]))
#	GPIO.output(11, val & (0x01 << 0))  
#	GPIO.output(12, val & (0x01 << 1))  
#	GPIO.output(13, val & (0x01 << 2))  
#	GPIO.output(15, val & (0x01 << 3))  
#	GPIO.output(16, val & (0x01 << 4))  
#	GPIO.output(18, val & (0x01 << 5))  
#	GPIO.output(22, val & (0x01 << 6))  
#	GPIO.output(7,  val & (0x01 << 7)) 

def loop():
	while True:
		for val in dats:
			writeOneByte(dats[val], pins=pins)
			time.sleep(0.5)

def destroy():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
		destroy()
