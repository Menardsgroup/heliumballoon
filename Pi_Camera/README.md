## Raspberry Pi Cameras

This is the bash shell script for Raspberry Pi cameras.

Note:
  - 40 seconds per picture
  - To execute: 
      - Enter "crontab -e" on terminal
      - Add this line at the end of crontab: "@reboot /bin/sh /home/pi/fin_code/launch_script.sh"
        and make sure to change the path
        
Update:

We changed it to the python3 script.
