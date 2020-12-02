#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

led = 21
btn = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
try:
	while True:
		GPIO.output(led, False)
		while GPIO.input(btn) == 1:
			GPIO.output(led, True)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("bye")
