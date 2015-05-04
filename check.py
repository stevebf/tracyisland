#!/usr/bin/env python

# Check the BT Home Hub router's home page to see which devices are connected
# to the network.  If a device is connected, turn on its LED.  If not, turn
# off its LED.

import urllib2
import RPi.GPIO as GPIO
import datetime
import time
import sys

time.sleep(10)

GPIO.setmode(GPIO.BOARD)

try:
    # create the lists of devices, owners and pins
    # Searching the HTML from the router will use a convention of putting
    # everything to lower case, to avoid missing a match because of a case
    # difference, so please make the device names lower case here.
    devicelist=["android-74e7b30847903cbd","stevemaesiphone","sarahs-ipad","davys-iphone"]
    pinlist=[15,16,18,22]
    ownerlist=["Richie","Steve","Sarah","Davy"]

    while True:
        # this is a file to which we'll write the output for debugging
        f = open('/home/pi/tracyisland/connecteddevices.txt', 'w')
        now = datetime.datetime.now()
        f.write(str(now)+"\n")
        print(now)

        # get data from page
        url = "http://bthomehub.home/index.cgi"
        response =  urllib2.urlopen(url)
        pagecontent = response.read().lower()

        # search for the devices.
        for i in range(len(devicelist)):

            GPIO.setup(pinlist[i], GPIO.OUT)

            if pagecontent.find(">" + devicelist[i] + "<")>0:
                # if the device is found, turn on the corresponding LED
                f.write(ownerlist[i] + " is here"+"\n")
                print(ownerlist[i] + " is here")
                GPIO.output(pinlist[i],True)
            else:
                # if the device is not found, turn on the corresponding LED
                f.write(ownerlist[i] + " is not here"+"\n")
                print(ownerlist[i] + " is not here")
                GPIO.output(pinlist[i],False)

        f.close

        time.sleep(10)

except:
    print 'Unexpected error:', sys.exc_info()[0]
    GPIO.cleanup()
