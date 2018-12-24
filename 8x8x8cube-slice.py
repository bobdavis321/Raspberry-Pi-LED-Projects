# 8x8x8 cube diagonal slice demo

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

# Create the patterns
L1 =[1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0,
	0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1]
L2 =[0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,
	0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0]
L3 =[0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0,
	0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0]
L4 =[0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0,
	0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0]
L5 =[0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,
	1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0]
L6 =[0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,
	0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0]
L7 =[0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,
	0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0]
L8 =[0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0, 0,0,1,0,0,0,0,0,
	0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0, 0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0]
# Set up so patterns can rotate
R1=L1
R2=L2
R3=L3
R4=L4
R5=L5
R6=L6
R7=L7
R8=L8
step=0

# set up loop
cycle= 0
while cycle < 100000:
  level = 0 
  while level < 8:
    # Send data to the display
    shift = 0
    while shift < 64:
      # determine if bit is set or clear data is not inverted
      GPIO.output(10, GPIO.LOW)
      if level ==0 and R1[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==1 and R2[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==2 and R3[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==3 and R4[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==4 and R5[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==5 and R6[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==6 and R7[shift] == 1: GPIO.output(10, GPIO.HIGH)
      if level ==7 and R8[shift] == 1: GPIO.output(10, GPIO.HIGH)
      # advance the clock
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      shift=shift+1
    # turn off the display 
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
  # change up the display
  if cycle%10 == 1: step=step+1
  if step == 8: step= 0
  if step == 0:
    R1=L1; R2=L2; R3=L3; R4=L4; R5=L5; R6=L6; R7=L7; R8=L8
  if step == 1:
    R1=L2; R2=L3; R3=L4; R4=L5; R5=L6; R6=L7; R7=L8; R8=L1
  if step == 2:
    R1=L3; R2=L4; R3=L5; R4=L6; R5=L7; R6=L8; R7=L1; R8=L2
  if step == 3:
    R1=L4; R2=L5; R3=L6; R4=L7; R5=L8; R6=L1; R7=L2; R8=L3
  if step == 4:
    R1=L5; R2=L6; R3=L7; R4=L8; R5=L1; R6=L2; R7=L3; R8=L4
  if step == 5:
    R1=L6; R2=L7; R3=L8; R4=L1; R5=L2; R6=L3; R7=L4; R8=L5
  if step == 6:
    R1=L7; R2=L8; R3=L1; R4=L2; R5=L3; R6=L4; R7=L5; R8=L6
  if step == 7:
    R1=L8; R2=L1; R3=L2; R4=L3; R5=L4; R6=L5; R7=L6; R8=L7
  cycle=cycle+1  

