# LED cube - Animated display
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

L1 =[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
L2 =[0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]
L3 =[0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]
L4 =[0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]
L5 =[0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0]
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
    # turn off display
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
  # change up the display
  if (cycle/20%10 == 1):
    R1=L1;    R2=L2;    R3=L3;    R4=L4;    R5=L5
  if (cycle/20%10 == 2):
    R1=L2;    R2=L3;    R3=L4;    R4=L5;    R5=L1
  if (cycle/20%10 == 3):
    R1=L3;    R2=L4;    R3=L5;    R4=L1;    R5=L2
  if (cycle/20%10 == 4):
    R1=L4;    R2=L5;    R3=L1;    R4=L2;    R5=L3
  if (cycle/20%10 == 5):
    R1=L5;    R2=L1;    R3=L2;    R4=L3;    R5=L4
  if (cycle/20%10 == 6):
    R1=L1;    R2=L2;    R3=L3;    R4=L4;    R5=L5
  if (cycle/20%10 == 7):
    R1=L2;    R2=L3;    R3=L4;    R4=L5;    R5=L1
  if (cycle/20%10 == 8):
    R1=L3;    R2=L4;    R3=L5;    R4=L1;    R5=L2
  if (cycle/20%10 == 9):
    R1=L4;    R2=L5;    R3=L1;    R4=L2;    R5=L3
  if (cycle/20%10 == 0):
    R1=L5;    R2=L1;    R3=L2;    R4=L3;    R5=L4
  cycle=cycle+1  

# end
