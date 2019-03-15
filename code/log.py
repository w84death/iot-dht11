#!/usr/bin/env python
from __future__ import print_function
import sys
import Adafruit_DHT
from subprocess import call
import datetime

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
report = '{2}: Temp {0:0.1f} C, Humidity {1:0.1f} %\n'.format(temperature, humidity, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
with open('/home/pi/code/readouts.log', 'a') as file:
    file.write(report)

