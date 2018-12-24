# LED cube 
# Uses 2x74595 and ULN2003
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Serial Data
GPIO.setup(18, GPIO.OUT) # L1
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Latch
GPIO.setup(23, GPIO.OUT) # L2
GPIO.setup(24, GPIO.OUT) # L3
GPIO.setup(25, GPIO.OUT) # L4
GPIO.setup(4,  GPIO.OUT) # L5

L1 =[0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]
L2 =[1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]
L3 =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
L4 =[1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]
L5 =[1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]
R1=L1
R2=L2
R3=L3
R4=L4
R5=L5

# set up the loop
cycle= 0
while cycle < 10000:
  level = 1 
  while level < 6:
    shift=0
    while shift < 16:
      # Send data to the shift register
      GPIO.output(17, GPIO.LOW)
      if level ==1:
        if R1[shift] == 1: GPIO.output(17, GPIO.HIGH)
      if level ==2:
        if R2[shift] == 1: GPIO.output(17, GPIO.HIGH)
      if level ==3:
        if R3[shift] == 1: GPIO.output(17, GPIO.HIGH)
      if level ==4:
        if R4[shift] == 1: GPIO.output(17, GPIO.HIGH)
      if level ==5:
        if R5[shift] == 1: GPIO.output(17, GPIO.HIGH)
      # advance the clock
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(27, GPIO.LOW)
      shift=shift+1
    # turn off the display
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    # latch and display the data
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    if level == 1: GPIO.output(18, GPIO.HIGH)
    if level == 2: GPIO.output(23, GPIO.HIGH)
    if level == 3: GPIO.output(24, GPIO.HIGH)
    if level == 4: GPIO.output(25, GPIO.HIGH)
    if level == 5: GPIO.output(4, GPIO.HIGH)
    time.sleep(.002)
    level = level+1
  cycle=cycle+1  

# end
