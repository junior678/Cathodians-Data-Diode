#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob
import os
import subprocess
import time
import sys

def HeartBeat ():
    x = 1
    while x == 1:
        file = open('heartbeat.txt','w')
        file.write('This hash identifies the 10 second heartbeat to Data Diode receiver: FdZq<Z:5k\~Jdq-_MW!dRmY{P')
        file.close() 
        os.system ("udp-sender --async --autostart 1 --max-bitrate 10m --fec 8x8 --file heartbeat.txt")
        os.remove ("heartbeat.txt")
        time.sleep(10)
HeartBeat()
