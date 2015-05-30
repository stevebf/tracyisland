Format the entire volume using Disk Utility on the mac.
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

# Git

Install git by typing

    sudo apt-get install git

Then set your identity by typing

    git config --global user.name "YOURNAME"
    git config --global user.email youremailaddress (I'm using gmail)

In the folder /home/pi, type

    git init

and then

    git clone https://github.com/stevebf/tracyisland

Note that now you have the .py file that you need.  You can edit on the Pi.

## Useful git commands

To check the status of your edits with respect to the repo:

    git status
    
To add changes to the staging area, so that your next commit will update your local repo:

    git add <filename>

To see what's in the staging area, again you can type     

    git status

Now you can commit everything that's staged, by typing

    git commit
    
If you've staged a file but want to unstage it, type

    git reaset HEAD <filename>
    
You can push committed changes to github with

    git push origin master
    
# Creating a Cron Jon
    
Now create a cron job to run the script, in the background, at startup:
- Start editing the crontab table by typing sudo crontab -e
- Arrow down to the end and add the line “@reboot python /home/pi/tracyisland/check.py &” (no quotes).  The & at the end tells it to run in the background.
- Add the line "0 3 * * * /sbin/shutdown -r now" to make the Pi reboot at 3am each morning. This is because the wifi dongle randomly goes down after a couple of days
- Save with “CTRL-X”, then “Y” and finally “Return”.

(The Pi drops the wifi from time to time. I did try to set up a crontab to check the network adaptor using the details at http://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/, but it didn't work.  If you revisit this, note that the BT Home Hub's address is 192.168.1.254.)

 
