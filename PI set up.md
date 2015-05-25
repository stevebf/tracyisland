Format the entire volume using Disk Utility.
- Run Disk Utility
- Select the Card Reader on the left-hand side
- Select the Erase tab
- Choose the format MS-DOS (FAT)
- Type a name (e.g. RASPPI)
- Click the “Erase…” button

Download NOOBS from https://www.raspberrypi.org/downloads/

Unzip the Zip file

Copy the contents of the zip file to the root of the SD card

Put the SD card into the Raspberry PI and boot up.

Monitor may have to be set to HDMI (it might be set up to expect VGA).

Select checkbox for Raspbian and choose the install button.
Default user is “pi”, with the user “raspberry”.

When install has finished, the PI runs the config program raspi-config.  You’ll want to:
- Enable Boot to Desktop
- set Internationalisation options (timezone and keyboard)

Create the folder /home/pi/tracyisland

Put the script check.py in this folder.

Now create a cron job to run the script, in the background, at startup:
- Start editing the crontab table by typing sudo crontab -e
- Arrow down to the end and add the line “@reboot python /home/pi/tracyisland/check.py &” (no quotes).  The & at the end tells it to run in the background.
- Add the line "0 15 * * * /sbin/shutdown -r now" to make the Pi reboot at 3am each morning. This is because the wifi dongle randomly goes down after a couple of days
- Save with “CTRL-X”, then “Y” and finally “Return”.

If you find the Pi drops the wifi from time to time, set up a crontab to check the network adaptor.  Details of how to do this are at http://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/.  Note that the BT Home Hub's address is 192.168.1.254.

 
