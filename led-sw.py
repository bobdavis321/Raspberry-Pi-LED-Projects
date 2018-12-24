import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT) #21 on older
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
# set pins as inputs with pull up resistors
GPIO.setup(7, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, GPIO.PUD_UP)

# set up loop
run=1
count=1
while count < 10:
  # check the status of the switches
  if GPIO.input(7)==0: run=1
  if GPIO.input(8)==0: run=0
  if run==1: count=count+1
  if count >8: count = 1
  # Turn everything off
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(27, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
  # Turn on selected LED
  if count==1: GPIO.output(17, GPIO.HIGH)
  if count==2: GPIO.output(18, GPIO.HIGH)
  if count==3: GPIO.output(27, GPIO.HIGH)
  if count==4: GPIO.output(22, GPIO.HIGH)
  if count==5: GPIO.output(23, GPIO.HIGH)
  if count==6: GPIO.output(24, GPIO.HIGH)
  if count==7: GPIO.output(25, GPIO.HIGH)
  if count==8: GPIO.output(4, GPIO.HIGH)
  time.sleep(.1)
# end 