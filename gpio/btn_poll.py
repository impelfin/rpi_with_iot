#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
count=0
try:
	while True:
		value = GPIO.input(26)
		if value == True:
			count += 1
			print count
			time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("bye")
