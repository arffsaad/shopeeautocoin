SHOPEE AUTO COIN COLLECTION V0.2

This program helps the you to collect shopee coins everyday at your preferred time of choosing. This can be set during first time setup.

PREREQUISITES:

- Python 3.9 (any latest version will do)
- Google Chrome (latest version)

ATTENTION:
CHROME MUST NOT BE USED WHEN SCRIPT IS TRIGGERED. IF SCRIPT IS TRIGGERED WHEN CHROME IS ALREADY RUNNING, SCRIPT WILL INVOKE AN ERROR.
Kindly close all chrome windows and re-run autocoin.py manually if this happens.

SETUP:

1. Install prerequisites first.
2. Place all files in the same directory.
3. Run "RUN FIRST.bat" as admin first. this will download and perform initial setup. Set a time for the script to run (USE HH:MM IN 24HR FORMAT ONLY)
4. Go to your downloads folder. Extract the chromedriver_win32.zip file that was downloaded.
5. Run config.py. Make sure everything is configured.
	- For username/password, fill in as needed.
	- For webdriverpath, point to "chromedriver.exe"
	- For OTP check, it will perform login. Please wait until a prompt appears. If an OTP is needed, type and press enter.
	- (if you always login shopee on chrome, this process will not ask for OTP)
6. Done! The script will run on the set time daily to collect coins.

TROUBLESHOOTING:

Chromedriver zip file does not exist in Downloads folder.
- Download the chromedriver manually from chromedriver website: https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip

Either files do not open properly at all (autocoin.py/config.py)
- right-click on affected file->Edit with IDLE->Edit with IDLE 3.9.X
- press F5
- Screenshot the error, and contact me at arffsaad@gmail.com
