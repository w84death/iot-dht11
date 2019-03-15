#!/usr/bin/env python
from __future__ import print_function
import sys
import Adafruit_DHT
from subprocess import call


humidity, temperature = Adafruit_DHT.read_retry(11, 4)
report = 'Odczyt. Temperatura {0:0.1f} stopni Celciusza. Wilgotnosc {1:0.1f} %'.format(temperature, humidity)
#print(report, file=sys.stderr)
call(["espeak","-vpl",report])
