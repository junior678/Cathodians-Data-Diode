#!/usr/bin/python3

import glob
import os
import subprocess

print("\n\nWelcome to The Cathodians Data Diode\n\n\nDo you wish to start a transfer?")

os.system("udp-sender --async --max-bitrate 10m --file name1.py")