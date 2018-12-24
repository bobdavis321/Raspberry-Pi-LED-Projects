# MCP3008 communication
# Prints teh contents of all 8 analog inputs.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.OUT) # Sclock
GPIO.setup(9, GPIO.IN) # MISO
GPIO.setup(10, GPIO.OUT) # MOSI 
GPIO.setup(8, GPIO.OUT) # CE0
port=0
serout=0x18

while port < 8:
  GPIO.output(8, GPIO.HIGH) # deselect chip
  GPIO.output(11, GPIO.LOW) # set clock low
  shift=0
  adcin=0
  # 24 pits shifted in and out
  while shift < 24:  
    GPIO.output(8, GPIO.LOW) # select chip
    # low for most bits out
    GPIO.output(10, GPIO.LOW) 
    if (shift == 7 or shift ==8): 
      GPIO.output(10, GPIO.HIGH)
    if shift == 9:
      if (port > 3): 
        GPIO.output(10, GPIO.HIGH)
    if shift == 10:
      if (port & 0x02): 
        GPIO.output(10, GPIO.HIGH)
    if shift == 11:
      if (port & 0x01): 
        GPIO.output(10, GPIO.HIGH)
    if shift > 13: # last 10 bits
      if(GPIO.input(9)):
        adcin = adcin+1 #set bit
      adcin = adcin << 1 # left shift 1
    # cycle the clock
    GPIO.output(11, GPIO.LOW) 
    GPIO.output(11, GPIO.HIGH) 
    shift=shift+1
  print adcin
  port=port+1
