import RPi.GPIO as GPIO
import time
# rows lit when high
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)#21 on older
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
#columns lit when low 
GPIO.setup(4, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

#GPIO.output(4, GPIO.LOW)
#GPIO.output(10, GPIO.LOW)
#GPIO.output(9, GPIO.LOW)
#GPIO.output(11, GPIO.LOW)
#GPIO.output(8, GPIO.LOW)

while True:
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.LOW)
   GPIO.output(9, GPIO.LOW)
   GPIO.output(11, GPIO.LOW)
   GPIO.output(8, GPIO.HIGH)
# turn on row1
   GPIO.output(25, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(25, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.HIGH)
   GPIO.output(9, GPIO.HIGH)
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)
# turn on row2
   GPIO.output(24, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(24, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.HIGH)
   GPIO.output(9, GPIO.HIGH)
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)
# turn on row3
   GPIO.output(23, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(23, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.LOW)
   GPIO.output(9, GPIO.LOW)
   GPIO.output(11, GPIO.LOW)
   GPIO.output(8, GPIO.HIGH)
# turn on row4
   GPIO.output(22, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(22, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.HIGH)
   GPIO.output(9, GPIO.HIGH)
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)
# turn on row5
   GPIO.output(27, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(27, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.HIGH)
   GPIO.output(9, GPIO.HIGH)
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)
# turn on row6
   GPIO.output(18, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(18, GPIO.LOW)
# next columns
   GPIO.output(4, GPIO.LOW)
   GPIO.output(10, GPIO.HIGH)
   GPIO.output(9, GPIO.HIGH)
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)
# turn on row7
   GPIO.output(17, GPIO.HIGH)
   time.sleep(.001)
   GPIO.output(17, GPIO.LOW)
# end
