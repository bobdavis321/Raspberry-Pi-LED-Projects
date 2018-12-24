import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Leading digit 0 or 1
GPIO.setup(1, GPIO.OUT)

# Second digit A-F
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# Third digit A-F
GPIO.setup(4, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)

# set up loop
count=0 
while count < 200:
  # turn everything off
  GPIO.output(1, GPIO.LOW)
  GPIO.output(0, GPIO.LOW)
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(21, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
  GPIO.output(7, GPIO.LOW)
  GPIO.output(8, GPIO.LOW)
  GPIO.output(9, GPIO.LOW)
  GPIO.output(10, GPIO.LOW)
  GPIO.output(11, GPIO.LOW)

  # turn on segments
  # First digit
  if count >= 100: 
    GPIO.output(1, GPIO.HIGH)

  # second digit divide by 10 then get right digit
  ccount=count/10%10
  if ccount==0: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH);GPIO.output(24, GPIO.HIGH)
  if ccount==1: 
    GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
  if ccount==2: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if ccount==3: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if ccount==4: 
    GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);
    GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if ccount==5: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH);
  if ccount==6: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if ccount==7: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
  if ccount==8: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if ccount==9: 
    GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);
    GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)

  # third digit get right digit
  ccount=count%10 
  if ccount==0: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.HIGH);GPIO.output(10, GPIO.HIGH);GPIO.output(11, GPIO.HIGH)
  if ccount==1: 
    GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH)
  if ccount==2: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  if ccount==3: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(9, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  if ccount==4: 
    GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH);
    GPIO.output(11, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  if ccount==5: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(8, GPIO.HIGH);GPIO.output(9, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH);GPIO.output(0, GPIO.HIGH);
  if ccount==6: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(8, GPIO.HIGH);GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH);GPIO.output(11, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  if ccount==7: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH)
  if ccount==8: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.HIGH);GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  if ccount==9: 
    GPIO.output(4, GPIO.HIGH);GPIO.output(7, GPIO.HIGH);GPIO.output(8, GPIO.HIGH);
    GPIO.output(11, GPIO.HIGH);GPIO.output(0, GPIO.HIGH)
  # delay
  time.sleep(1)
  count=count+1

