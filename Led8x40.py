# LED 8x40 Dual Color array
# Uses individual letters strung together
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Red Data
GPIO.setup(18, GPIO.OUT) # Green Data
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Latch
GPIO.setup(23, GPIO.OUT) # Row Data 1
GPIO.setup(24, GPIO.OUT) # Row Data 2
GPIO.setup(25, GPIO.OUT) # Row Data 4
GPIO.setup(4, GPIO.OUT) # Row Enable

A1 =[0,0,0,0,0]
A2 =[0,0,1,0,0]
A3 =[0,1,0,1,0]
A4 =[1,0,0,0,1]
A5 =[1,1,1,1,1]
A6 =[1,0,0,0,1]
A7 =[1,0,0,0,1]
A8 =[1,0,0,0,1]

B1 =[0,0,0,0,0]
B2 =[1,1,1,1,0]
B3 =[1,0,0,0,1]
B4 =[1,0,0,0,1]
B5 =[1,1,1,1,0]
B6 =[1,0,0,0,1]
B7 =[1,0,0,0,1]
B8 =[1,1,1,1,0]

E1 =[0,0,0,0,0]
E2 =[1,1,1,1,1]
E3 =[1,0,0,0,0]
E4 =[1,0,0,0,0]
E5 =[1,1,1,1,0]
E6 =[1,0,0,0,0]
E7 =[1,0,0,0,0]
E8 =[1,1,1,1,1]

P1 =[0,0,0,0,0]
P2 =[1,1,1,1,0]
P3 =[1,0,0,0,1]
P4 =[1,0,0,0,1]
P5 =[1,1,1,1,0]
P6 =[1,0,0,0,0]
P7 =[1,0,0,0,0]
P8 =[1,0,0,0,0]

R1 =[0,0,0,0,0]
R2 =[1,1,1,1,0]
R3 =[1,0,0,0,1]
R4 =[1,0,0,0,1]
R5 =[1,1,1,1,0]
R6 =[1,0,0,0,1]
R7 =[1,0,0,0,1]
R8 =[1,0,0,0,1]

S1 =[0,0,0,0,0]
S2 =[0,1,1,1,1]
S3 =[1,0,0,0,0]
S4 =[1,0,0,0,0]
S5 =[0,1,1,1,0]
S6 =[0,0,0,0,1]
S7 =[0,0,0,0,1]
S8 =[1,1,1,1,0]

Y1 =[0,0,0,0,0]
Y2 =[1,0,0,0,1]
Y3 =[1,0,0,0,1]
Y4 =[0,1,0,1,0]
Y5 =[0,0,1,0,0]
Y6 =[0,0,1,0,0]
Y7 =[0,0,1,0,0]
Y8 =[0,0,1,0,0]

# Z is used as a blank
Z1 =[0,0,0,0,0]
Z2 =[0,0,0,0,0]
Z3 =[0,0,0,0,0]
Z4 =[0,0,0,0,0]
Z5 =[0,0,0,0,0]
Z6 =[0,0,0,0,0]
Z7 =[0,0,0,0,0]
Z8 =[0,0,0,0,0]

Red1=R1+Z1+S1+P1+Z1+E1+R1+Z1
Red2=R2+Z2+S2+P2+Z2+E2+R2+Z2
Red3=R3+Z3+S3+P3+Z3+E3+R3+Z3
Red4=R4+Z4+S4+P4+Z4+E4+R4+Z4
Red5=R5+Z5+S5+P5+Z5+E5+R5+Z5
Red6=R6+Z6+S6+P6+Z6+E6+R6+Z6
Red7=R7+Z7+S7+P7+Z7+E7+R7+Z7
Red8=R8+Z8+S8+P8+Z8+E8+R8+Z8

Green1=R1+A1+Z1+P1+B1+Z1+R1+Y1
Green2=R2+A2+Z2+P2+B2+Z2+R2+Y2
Green3=R3+A3+Z3+P3+B3+Z3+R3+Y3
Green4=R4+A4+Z4+P4+B4+Z4+R4+Y4
Green5=R5+A5+Z5+P5+B5+Z5+R5+Y5
Green6=R6+A6+Z6+P6+B6+Z6+R6+Y6
Green7=R7+A7+Z7+P7+B7+Z7+R7+Y7
Green8=R8+A8+Z8+P8+B8+Z8+R8+Y8

# set up the loop
cycle= 0
while cycle < 1000:
  row = 0 
  while row <9:
    row = row+1
    # Send data to the shift registers
    shift = 39
    while shift >= 0:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        # determine if bit is set or clear data is NOT inverted
        if row==1:
          if Red1[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green1[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==2:
          if Red2[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green2[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==3:
          if Red3[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green3[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==4:
          if Red4[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green4[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==5:
          if Red5[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green5[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==6:
          if Red6[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green6[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==7:
          if Red7[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green7[shift] == 1: GPIO.output(18, GPIO.HIGH)
        if row==8:
          if Red8[shift] == 1: GPIO.output(17, GPIO.HIGH)
          if Green8[shift] == 1: GPIO.output(18, GPIO.HIGH)
        # advance the clock
        GPIO.output(27, GPIO.HIGH); GPIO.output(27, GPIO.LOW)
        shift=shift-1
    # select the row data is inverted 
    GPIO.output(4, GPIO.HIGH) # Turn off display
    if row==2: GPIO.output(23, GPIO.LOW); GPIO.output(24, GPIO.HIGH); GPIO.output(25, GPIO.HIGH)
    if row==3: GPIO.output(23, GPIO.HIGH); GPIO.output(24, GPIO.LOW); GPIO.output(25, GPIO.HIGH)
    if row==4: GPIO.output(23, GPIO.LOW); GPIO.output(24, GPIO.LOW); GPIO.output(25, GPIO.HIGH)
    if row==5: GPIO.output(23, GPIO.HIGH); GPIO.output(24, GPIO.HIGH); GPIO.output(25, GPIO.LOW)
    if row==6: GPIO.output(23, GPIO.LOW); GPIO.output(24, GPIO.HIGH); GPIO.output(25, GPIO.LOW)
    if row==7: GPIO.output(23, GPIO.HIGH); GPIO.output(24, GPIO.LOW); GPIO.output(25, GPIO.LOW)
    if row==8: GPIO.output(23, GPIO.LOW); GPIO.output(24, GPIO.LOW); GPIO.output(25, GPIO.LOW)
    # latch and display the data
    GPIO.output(22, GPIO.LOW); GPIO.output(22, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW) # Turn back on
    # time.sleep(.0005)
  cycle=cycle+1  

