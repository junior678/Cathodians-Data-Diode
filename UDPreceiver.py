#!/usr/bin/python3

import RPi.GPIO as GPIO
import glob
import os
import subprocess
import time
from datetime import datetime
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) #Green LED Used to Indicate File Activity
GPIO.setup(18,GPIO.OUT) #Red LED Used to Indicate HeartBeat Failure
GPIO.setup(26,GPIO.OUT) #Yellow LED Used to Indicate HeartBeat Activity

#This function receives input from the user and outputs it to the udpcast command

def DiodeReceive():
    count=1
    file="file"
    while True:
        if (os.path.exists(file + str(count))):
            count = count + 1
        print("\nThe Cathodians Data Diode Receiver is Listening\n\n\n")
        os.system ("udp-receiver --file " +str(file) + str(count))
        if 'FdZq<Z:5k\~Jdq-_MW!dRmY{P' in open(file +str(count)).read():
	    os.rename ('file' +str(count), 'HeartBeat')
            print "*----PULSE YELLOW LED INDICATING HEARTBEAT ACTIVITY----*\n\n"
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
	else:
            count = count + 1
            print "*----PULSE GREEN LED INDICATING DIODE FILE RECEVING ACTIVITY----*\n\n"
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)

def HeartBeatReceive():
    count=1
    file="file"
    while True:
        if (os.path.exists(file + str(count))):
            count = count + 1
        print("\nThe Cathodians Data Diode Receiver is Listening\n\n\n")
        os.system ("udp-receiver --portbase 9002 --file " +str(file) + str(count))
        if 'FdZq<Z:5k\~Jdq-_MW!dRmY{P' in open(file +str(count)).read():
	    os.rename ('file' +str(count), 'HeartBeat')
            print "*----PULSE YELLOW LED INDICATING HEARTBEAT ACTIVITY----*\n\n"
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(26,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(26,GPIO.LOW)
	else:
            count = count + 1
            print "*----PULSE GREEN LED INDICATING DIODE FILE RECEVING ACTIVITY----*\n\n"
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)
            time.sleep(.25)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(17,GPIO.LOW)

def HeartBeatAlert():
    while True:
        now = time.time()
        thirty_seconds = now - 30
        last_heart_beat = os.path.getmtime("HeartBeat")

        while last_heart_beat < thirty_seconds:
            print "*---HEARTBEAT IS DOWN, RED LED ON---*"
            GPIO.output(18,GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(.5)
            print(thirty_seconds)
            print(last_heart_beat)
            return HeartBeatAlert()

if True:
    Process(target=DiodeReceive).start()
    Process(target=HeartBeatReceive).start()
    Process(target=HeartBeatAlert).start()
