# 8x8x8 cube random rain demo

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
import random

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

# create random numbers
rnum1 = random.randrange(0, 64, 1) 
rnum2 = random.randrange(0, 64, 1) 
rnum3 = random.randrange(0, 64, 1) 
rnum4 = random.randrange(0, 64, 1) 
rnum5 = random.randrange(0, 64, 1) 
rnum6 = random.randrange(0, 64, 1) 
rnum7 = random.randrange(0, 64, 1) 
rnum8 = random.randrange(0, 64, 1) 

# set up loop
cycle= 0
while cycle < 100000:
  level = 0 
  while level < 8:
    # Send data to the arrays
    shift = 0
    while shift < 64:
      # determine if bit is set or clear 
      GPIO.output(10, GPIO.LOW)
      # Send data to the shift registers
      if level == 0:
        if rnum1 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 1: 
        if rnum2 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 2: 
        if rnum3 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 3: 
        if rnum4 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 4:
        if rnum5 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 5: 
        if rnum6 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 6:
        if rnum7 == shift: GPIO.output(10, GPIO.HIGH)
      if level == 7: 
        if rnum8 == shift: GPIO.output(10, GPIO.HIGH)
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
  # shift random numbers
  if cycle%10 == 1 or cycle%10 == 5:
    rnum8 = rnum7
    rnum7 = rnum6 
    rnum6 = rnum5 
    rnum5 = rnum4 
    rnum4 = rnum3 
    rnum3 = rnum2 
    rnum2 = rnum1 
    rnum1 = random.randrange(0, 64, 1) 
  cycle=cycle+1  

