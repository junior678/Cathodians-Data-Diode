
#!/usr/bin/python3

import glob
import os
import subprocess

print("\nWelcome to The Cathodians Data Diode\n\n\n?")

#This function receives input from the user and outputs it to the udpcast command

def Main ():
    count=1
    while (count < 20):

        os.system ("udp-receiver --file file"+str(count))
        count = count + 1
    print "Thank you for using The Cathodians Data Diode!"
        


Main()
