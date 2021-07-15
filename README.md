# SHOPEE AUTO COIN COLLECTION V1.0

* This program helps you to collect shopee coins everyday at your preferred time of choosing. This can be set during first time setup.

### UPDATE V1.0:
The script now uses its own data-directory, copied from localappdata. Now the script can run regardless of any chrome window currently running.

## PREREQUISITES:

* Python 3.9 (any latest version will do)
* Google Chrome (latest version)

## SETUP:

1. Install prerequisites first.
2. Extract everything in the same folder.
3. Run "RUN FIRST.bat" as admin. this will download chromedriver_win32.zip and perform initial setup. Set a time for the script to run (USE HH:MM IN 24HR FORMAT ONLY)
4. Extract the chromedriver_win32.zip file that was downloaded.
5. Run config.py. Make sure everything is configured.
	- For username/password, fill in as needed.
	- For webdriverpath, point to "chromedriver.exe"
	- For OTP check, it will perform login. Please wait until a prompt appears. If an OTP is needed, type and press enter.
	- (if you always login shopee on chrome, this process will not ask for OTP)
6. Done! The script will run on the set time daily to collect coins.

## TROUBLESHOOTING:

Chromedriver zip file does not exist in Downloads folder.
- Download the chromedriver manually from chromedriver website: https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip

Either files do not open properly at all (autocoin.py/config.py)
- right-click on affected file->Edit with IDLE->Edit with IDLE 3.9.X
- press F5
- Screenshot the error, and contact me at arffsaad@gmail.com
