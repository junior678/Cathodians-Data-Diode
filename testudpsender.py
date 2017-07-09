#!/usr/bin/python3

import glob
import os
import subprocess
import time
import sys

print("\nWelcome to The Cathodians Data Diode\n\n")

#This function receives input from the user and outputs it to the udpcast command

def Main ():
    while True:
        try:
            u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))
            break
        except:
            print("\n\nThat's not a valid option!")
            u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))

    if u_input == 1:
        f_input = raw_input("Please enter filename: ")
        os.system ("udp-sender --async --max-bitrate 10m --file "+f_input)
        return Main()

    elif u_input == 2:
        print('Thank you for using The Cathodians Data Diode! Program will close in 3 seconds.')
        print('1')
        time.sleep(.5)
        print('...')
        time.sleep(.5)
        print('2')
        time.sleep(.5)
        print('...')
        time.sleep(.5)
        print('3')
        time.sleep(.5)
        print('Goodbye.')
        time.sleep(.5)
        sys.exit()
    else:
	print("\n\nThat's not a valid option!")
        u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))


       
    while True:
        try:
            u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))
            break
        except:
            print("\n\nThat's not a valid option!")
            u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))
    if u_input == 1:
        f_input = raw_input("Please enter filename: ")
        os.system ("udp-sender --async --max-bitrate 10m --file "+f_input)

    elif u_input == 2:
        print('Thank you for using The Cathodians Data Diode!')
    else:
	print("\n\nThat's not a valid option!")
        u_input = int(input('Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n'))



Main()
