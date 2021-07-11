SHOPEE AUTO COIN COLLECTION V0.2

This program helps the you to collect shopee coins everyday at your preferred time of choosing. This can be set during first time setup.

PREREQUISITES:

- Python 3.9 (any latest version will do)
- Google Chrome (latest version)

SETUP:

1. Install prerequisites first. 
1. Run "RUN FIRST.bat" as admin first. this will download and perform initial setup. Set a time for the script to run (USE HH:MM IN 24HR FORMAT ONLY)
2. Go to your downloads folder. Extract the zip file that was downloaded.
3. Run config.py. Make sure everything is configured.
	i.	For username/password, fill in as needed.
	ii.	For webdriverpath, point to "chromedriver.exe"
	iii.	For OTP check, it will perform login. Please wait until a prompt appears. If an OTP is needed, type and press enter.
		(if you always login shopee on chrome, this process will not ask for OTP)
4. Done! The script will run on the set time daily to collect coins.

TROUBLESHOOTING:

Chromedriver zip file does not exist in Downloads folder.
- Download the chromedriver manually from chromedriver website: https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip

Either files do not open properly at all (autocoin.py/config.py)
- right-click on affected file->Edit with IDLE->Edit with IDLE 3.9.X
- press F5
- Screenshot the error, and contact me at arffsaad@gmail.com
