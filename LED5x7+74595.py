# LED 5x7 array with 74595
# Uses 74595 Shift Register
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Serial Data
GPIO.setup(18, GPIO.OUT) # C1
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Latch
GPIO.setup(23, GPIO.OUT) # C2
GPIO.setup(24, GPIO.OUT) # C3
GPIO.setup(25, GPIO.OUT) # C4
GPIO.setup(4, GPIO.OUT) # C5

R1 =[1,1,1,1,0,
         1,0,0,0,1,
         1,0,0,0,1,
         1,1,1,1,0,
         1,0,0,0,1,
         1,0,0,0,1,
         1,0,0,0,1]

# set up the loop
cycle= 0
while cycle < 10000:
  row = 0 
  while row < 7:
    # determine if bit is set or clear low=lit 
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
    if R1[row*5] == 1: GPIO.output(18, GPIO.LOW)
    if R1[1+row*5] == 1: GPIO.output(23, GPIO.LOW)
    if R1[2+row*5] == 1: GPIO.output(24, GPIO.LOW)
    if R1[3+row*5] == 1: GPIO.output(25, GPIO.LOW)
    if R1[4+row*5] == 1: GPIO.output(4, GPIO.LOW)
    # Send data to the shift register
    GPIO.output(17, GPIO.LOW)
    if row==0: GPIO.output(17, GPIO.HIGH)
    # advance the clock
    GPIO.output(27, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    # latch and display the data
    GPIO.output(22, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(.001)
    row = row+1
  cycle=cycle+1  


