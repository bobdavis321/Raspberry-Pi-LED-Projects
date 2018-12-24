# LED7segTime
# Uses segment strings strung together
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) # Serial Data
GPIO.setup(18, GPIO.OUT) # 
GPIO.setup(27, GPIO.OUT) # Clock, 21 on older 
GPIO.setup(22, GPIO.OUT) # Latch

# Segments 1 nul then: G-F-E-D-C-B-A
Nums = {'0':(0,0,1,1,1,1,1,1),
                '1':(0,0,0,0,0,1,1,0),
                '2':(0,1,0,1,1,0,1,1),
                '3':(0,1,0,0,1,1,1,1),
                '4':(0,1,1,0,0,1,1,0),
                '5':(0,1,1,0,1,1,0,1),
                '6':(0,1,1,1,1,1,0,1),
                '7':(0,0,0,0,0,1,1,1),
                '8':(0,1,1,1,1,1,1,1),
                '9':(0,1,1,0,0,1,1,1)}

print 'the current time is: ' 
print time.strftime( '%H:%M:%S' )

# set up the loop
while True:
    tstr=time.strftime( '%H:%M:%S')
    Data1=Nums[tstr[0]]+Nums[tstr[1]]+Nums[tstr[3]]+Nums[tstr[4]]+Nums[tstr[6]]+Nums[tstr[7]]
    # Send data to the shift registers
    shift = 47
    while shift >= 0:
        GPIO.output(17, GPIO.LOW)
        # determine if bit is set or clear data is NOT inverted
        if Data1[shift] == 1: GPIO.output(17, GPIO.HIGH)
        # advance the clock
        GPIO.output(27, GPIO.LOW); GPIO.output(27, GPIO.HIGH)
        shift=shift-1
    # Latch and display the output
    GPIO.output(22, GPIO.LOW); GPIO.output(22, GPIO.HIGH)
    time.sleep(.1)

