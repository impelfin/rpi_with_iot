#!/usr/bin/env python

import RPIO 
import time

RPIO.setmode(RPIO.BCM)
RPIO.setup(21, RPIO.OUT)
while(True):
	RPIO.output(21,True)
	time.sleep(1)
	RPIO.output(21,False)
	time.sleep(1)
