# LED 8x15 Dual Color array

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Red Data
GPIO.setup(18, GPIO.OUT) # Green Data
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Enable
GPIO.setup(23, GPIO.OUT) # Row Data
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

Redbyte1 =[0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1]
Redbyte2 =[0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1]
Redbyte3 =[0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1]
Redbyte4 =[0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1]
Redbyte5 =[0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1]
Redbyte6 =[0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1]
Redbyte7 =[0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1]
Redbyte8 =[0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]

Greenbyte1 =[0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte2 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte3 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte4 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte5 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte6 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte7 =[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
Greenbyte8 =[0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0]

Rowbyte1 =[0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
Rowbyte2 =[0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
Rowbyte3 =[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]
Rowbyte4 =[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]
Rowbyte5 =[0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
Rowbyte6 =[0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]
Rowbyte7 =[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]
Rowbyte8 =[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]

# set up loop
cycle= 0
while cycle < 100000:
  row = 0 
  while row < 8:
    row = row+1
    # Send data to the display
    shift = 15
    while shift > 0:
        # determine if bit is set or clear data is inverted
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        # Send data to shift registers
        if row==1:
            if Redbyte1[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte1[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte1[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==2:
            if Redbyte2[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte2[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte2[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==3:
            if Redbyte3[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte3[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte3[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==4:
            if Redbyte4[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte4[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte4[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==5:
            if Redbyte5[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte5[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte5[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==6:
            if Redbyte6[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte6[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte6[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==7:
            if Redbyte7[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte7[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte7[shift] == 1: GPIO.output(23, GPIO.HIGH)
        if row==8:
            if Redbyte8[shift] == 1: GPIO.output(17, GPIO.LOW)
            if Greenbyte8[shift] == 1: GPIO.output(18, GPIO.LOW)
            if Rowbyte8[shift] == 1: GPIO.output(23, GPIO.HIGH)
        # advance the clock
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        shift=shift-1
    # latch and display the data
    GPIO.output(22, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
#    time.sleep(.001)
  cycle=cycle+1  

