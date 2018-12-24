import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)

# set up loop
count=0 
while count < 10:
  count=count+1
  # turn everything off
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(21, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)

  # turn on segments
  if count==1: GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
  if count==2: GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if count==3: GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if count==4: GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if count==5: GPIO.output(17, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(22, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH);
  if count==6: GPIO.output(17, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH)
  if count==6: GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if count==7: GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH)
  if count==8: GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
  if count==8: GPIO.output(23, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  if count==9: GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(21, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
  # delay
  time.sleep(1)
