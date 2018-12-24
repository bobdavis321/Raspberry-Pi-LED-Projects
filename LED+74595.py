# LED with 74595
# Uses 74595 Shift Registers
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Serial Data
GPIO.setup(18, GPIO.OUT) # 
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Latch

# set up the loop
cycle= 0
scan = 1
direction=0

while cycle < 1000:
    if scan==24:
        direction=0
    if scan==0:
        direction=1
    # Send data to the shift registers
    shift = 24
    while shift >= 0:
        GPIO.output(17, GPIO.LOW)
        # determine if bit is set or clear 
        if shift <= scan: 
            GPIO.output(17, GPIO.HIGH)
        # advance the clock
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(27, GPIO.HIGH)
        shift=shift-1
    # Latch and display the output
    GPIO.output(22, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    if direction==0:scan=scan-1
    if direction==1:scan=scan+1
    time.sleep(.05)
    cycle=cycle+1  

