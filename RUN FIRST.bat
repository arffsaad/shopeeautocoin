@echo off
pip install selenium
IF NOT EXIST "%userprofile%\Downloads\chromedriver_win32.zip" bitsadmin /transfer ChromeDriverDownload /download /priority normal https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip %userprofile%\Downloads\chromedriver_win32.zip
set /p tme="Enter the time you wish to collect coins(in HH:MM, 24HR format): "
SCHTASKS /CREATE /SC DAILY /TN "Autocoin\shopeecollect" /TR "%cd%\autocoin.py" /ST %tme%
CLS
ECHO Creating usrdata...
MKDIR usrdata
xcopy /s "%localappdata%\Google\Chrome\User Data" "%cd%\usrdata\"
CLS
ECHO First time setup done! Press enter to quit...
PAUSE
