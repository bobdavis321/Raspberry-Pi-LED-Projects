# 8x8x8 cube random demo

import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # layer 1
GPIO.setup(18, GPIO.OUT) # layer 2
GPIO.setup(27, GPIO.OUT) # layer 3
GPIO.setup(22, GPIO.OUT) # layer 4
GPIO.setup(23, GPIO.OUT) # layer 5
GPIO.setup(24, GPIO.OUT) # layer 6
GPIO.setup(25, GPIO.OUT) # layer 7
GPIO.setup(4, GPIO.OUT) # layer 8
GPIO.setup(9, GPIO.OUT) # latch
GPIO.setup(10, GPIO.OUT) # data
GPIO.setup(11, GPIO.OUT) # clock

# set up loop
cycle= 0
while cycle < 100000:
  level = 0 
  while level < 8:
    # Send data to the display
    shift = 0
    while shift < 64:
        # determine if bit is set or clear data is inverted
        GPIO.output(10, GPIO.LOW)
        rnum = random.randrange(0, 64, 1) 
       # Send data to shift registers
        if rnum == shift: GPIO.output(10, GPIO.HIGH)
        # advance the clock
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        shift=shift+1
    # turn off display 
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    # latch and display the data
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW)
    if level == 0:  GPIO.output(17, GPIO.HIGH)
    if level == 1:  GPIO.output(18, GPIO.HIGH)
    if level == 2:  GPIO.output(27, GPIO.HIGH)
    if level == 3:  GPIO.output(22, GPIO.HIGH)
    if level == 4:  GPIO.output(23, GPIO.HIGH)
    if level == 5:  GPIO.output(24, GPIO.HIGH)
    if level == 6:  GPIO.output(25, GPIO.HIGH)
    if level == 7:  GPIO.output(4, GPIO.HIGH)
    level = level+1
    time.sleep(.01)
  cycle=cycle+1  

