import tkinter as tk
from tkinter import filedialog
from time import sleep as sl
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

usrdir = ('--user-data-dir=' + os.getcwd() + r"\usrdata")
status = [0,0,0,0]
check = [6,7,10,11]
stat = ["NOT CONFIGURED", "CONFIGURED"]
count = 0
lang = '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button'
verify = '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button'

option = webdriver.ChromeOptions()
option.add_argument(usrdir)
option.add_argument(r"--profile-directory=Default")
option.add_argument("--log-level=3")
option.add_argument("--disable-extensions")
option.add_argument("--disable-gpu")
option.add_argument("--headless")
option.add_argument('--window-size=1920,1080')



# reading oldparams
f = open('params.txt','r')
pars = f.readlines()
f.close()

for x in check:
    if (pars[x] != "na\n"):
        status[count] = 1
        count = count + 1

print("AUTOCOIN CONFIG\nUsername: ", stat[status[0]], "\nPassword: ", stat[status[1]], "\nWebdriver: ", stat[status[2]], "\nOTP Check: ", stat[status[3]])

print("\n\n[1] Set Login Credentials\n[2] Set webdriver path\n[3] Configure OTP checking")
menu = input(">>>")

if (menu == "1"):
    pars[6] = input("Enter phone number/username: ")
    pars[7] = input("Enter password: ")
    pars[6] = pars[6] + "\n"
    pars[7] = pars[7] + "\n"
if (menu=="3"):
    driverpath = pars[10][0:-1]
    driver = webdriver.Chrome(executable_path=driverpath, options=option)
    driver.get(pars[8])
    sl(3)
    if(driver.current_url == pars[8][0:-1]):
        try:
            driver.find_element_by_xpath(lang).click()
        except:
            nan = 0
        sl(2)
        driver.find_element_by_xpath(pars[1]).send_keys(pars[6])
        sl(1)
        driver.find_element_by_xpath(pars[2]).send_keys(pars[7])
        driver.find_element_by_xpath(pars[3]).click()
        if (driver.current_url != pars[9][0:-1]):
            otp =  input("First Login! Please input OTP here: ")
            driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[3]/input[2]').click()
            sendotp = ActionChains(driver)
            sendotp.send_keys(otp)
            sendotp.perform()
            sl(1)
            driver.find_element_by_xpath(verify).click()
    pars[11] = "done\n"        
elif (menu == "2"):
    #ONLY FOR DRIVERPATH#
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    pars[10] = file_path + "\n"
    #DRIVERPATH END#

with open('params.txt', 'w') as f:
    for item in pars:
        f.write(item)

print("Done! Exiting config...")
sl(3)
driver.quit()
