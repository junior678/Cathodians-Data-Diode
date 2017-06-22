#!/usr/bin/python3

import glob
import os
import subprocess

print("\nWelcome to The Cathodians Data Diode\n\n\n?")

#This function receives input from the user and outputs it to the udpcast command

def Main ():
    u_input = input("Do you wish to start a transfer?\n\n(1) YES\n\n(2) NO\n\n ")
    if u_input == 1 :
        f_input = raw_input("Please enter filename: ")
        os.system ("udp-sender --async --max-bitrate 10m --file "+f_input)


Main()
