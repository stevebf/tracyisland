# tracyisland

## 19/8/2014
Code reads the HTML from the BT Home Hub and searches it for the required devices.
If a device is found, it turns on the corresponding LED, and if it doesn't find it it turns that LED off.
The devices that it searches for are Steve and Davy's iPhones, Sarah's iPad, and Richie's Galaxy.
Richie's Galaxy drops off the network when its screen turns off, so it's not particularly useful in Richie's case.

Backups are done to dropbox, but so far I haven't got a way of doing this automatically, so please backup by uploading the files in the TracyIsland folder manually at the end of each session.

## 22/8/2014
Frame arrived from ebay

## 23/8/2014
Changed python script to add a datestamp to the log file connected.txt

Added cron script by running crontab -e

You can check the cron jobs you have in place by running crontab -l

The cron scripts that I now have in place are

\* * * * * cd /home/pi/tracyisland; sudo python check.py

\* * * * * sleep 20; cd /home/pi/tracyisland; sudo python check.py

\* * * * * sleep 40; cd /home/pi/tracyisland; sudo python check.py

## 24/8/2014
Built the breadboard to show the LEDs

Took the GPIO.cleanup() line out of the python script, because if I don't then the LED doesn't stay on when the script ends

## 1/11/2014
The VNC Server is now working, but I have to log on to the RPi as "root".  The problem where I couldn't ping the RPi was solved when I restarted the router, so this might need to be a regular thing if I can't VNC to the Pi in future.

Problem where the boot sequence said the device hadn't been shutdown problem: www.raspberrypi.org/forums/viewtopic.php?p=495156 (post by rtek1000).

## 05/4/2015

Soldered everything into place.

* Pin 15 (Richie) = GPIO22 - blue wire
* Pin 16 (Steve) = GPIO23 - green wire
* Pin 18 (Sarah) = GPIO24 - orange wire
* Pin 22 (Davy) = GPIO25 - yellow wire

## 4/5/2015

Rewrote script to  run once on startup instead of running a single instance every 20 seconds

