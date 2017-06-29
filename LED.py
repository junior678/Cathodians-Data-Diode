import RPi.GPIO as GPIO
import time
x = 1
while x == 1:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    print ("LED on")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(.5)
    print ("LED off")
    GPIO.output(17,GPIO.LOW)
    time.sleep(1)
