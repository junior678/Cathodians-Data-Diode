#!/usr/bin/python3
import RPI.GPIO as GPIO
import time
import glob
import os
import subprocess

print("\nWelcome to The Cathodians Data Diode\n\n\n?")

#This function receives input from the user and outputs it to the udpcast command

def Main ():
    count=1
    file="testfile"
    while (count < 4 ):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT)
        if (os.path.exists(file + str(count))):
            count = count + 1
        os.system ("udp-receiver --interface eth1 --file " +str(file) + str(count$
        if 'secret code' in open(file +str(count)).read():
            print "\n\n-------------------\nTHIS IS \n     THE HEARTBEAT"
            print "--------------------"
            print "*----GREEN LED ON-----*"
            GPIO.output(17,GPIO.HIGH)   # Select pin for GREEN LED
            time.sleep(1)
            GPIO.output(17,LOW)
        count = count + 1
        print "*----YELLOW LED ON----*\n\n"
        GPIO.output(17,GPIO.HIGH)       # Select pin for YELLOW LED
        time.sleep(2)
        GPIO.output(17,LOW)
    print "Thank you for using The Cathodians Data Diode!\n"
Main()
