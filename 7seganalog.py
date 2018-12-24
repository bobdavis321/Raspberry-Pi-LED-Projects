# 7 Segment Analog
# Read analog port 0 and display the results

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Segments A-F
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT) #21 on older
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT) 
# digit selection pins
GPIO.setup(4, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
# Analog pins
GPIO.setup(11, GPIO.OUT) # Sclock
GPIO.setup(9, GPIO.IN) # MISO
GPIO.setup(10, GPIO.OUT) # MOSI 
GPIO.setup(8, GPIO.OUT) # CE0
port=0
serout=0x18

# set up loop
cycle=0 
while cycle < 10:
  # only sample every 10 times through
  cycle=cycle+1
  if cycle == 10: cycle = 0
  if cycle == 1:
    # Read analog data
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
  digit=1
  while digit < 4:
    # turn everything off
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW) 
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)

    if digit == 1:
      # first digit get right most digit
      ccount=adcin%10
      GPIO.output(2, GPIO.HIGH) 
    if digit == 2:
      # second digit divide by 10 then get digit
      ccount=adcin/10%10
      GPIO.output(3, GPIO.HIGH)
    if digit == 3:
      # third digit divide by 100 then get digit
      ccount=adcin/100%10
      GPIO.output(4, GPIO.HIGH)
    # turn on segments
    if ccount==0: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH);GPIO.output(24, GPIO.HIGH)
    if ccount==1: 
      GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH)
    if ccount==2: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    if ccount==3: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    if ccount==4: 
      GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH);
      GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    if ccount==5: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(27, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
      GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH);
    if ccount==6: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(27, GPIO.HIGH);GPIO.output(22, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH);GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    if ccount==7: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH)
    if ccount==8: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH);GPIO.output(23, GPIO.HIGH)
      GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    if ccount==9: 
      GPIO.output(17, GPIO.HIGH);GPIO.output(18, GPIO.HIGH);GPIO.output(27, GPIO.HIGH);
      GPIO.output(24, GPIO.HIGH);GPIO.output(25, GPIO.HIGH)
    digit=digit+1 
    time.sleep(.005)
# end



