from time import sleep
from selenium import webdriver
from os import system
import os

# reading params
f = open('params.txt','r')
pars = f.readlines()

# vars

coin = pars[0]
usr = pars[1]
psw = pars[2]
login = pars[3]
amount = pars[4]
total = pars[5]
usrn = pars[6]
pswd = pars[7]
loginURL = pars[8][0:-1]
coinURL = pars[9]
driverpath = pars[10][0:-1]
usrdir = ('--user-data-dir=' + os.getcwd() + r"\usrdata")

f.close()
# end var

option = webdriver.ChromeOptions()
option.add_argument(usrdir)
option.add_argument(r"--profile-directory=Default")
option.add_argument("--log-level=3")
option.add_argument("--disable-extensions")
option.add_argument("--disable-gpu")
option.add_argument("--headless")
option.add_argument('--window-size=1920,1080')
option.add_argument('--remote-debugging-port=54332')

driver = webdriver.Chrome(executable_path=driverpath, options=option)

system('cls')
print("Shopee Daily Autocoin Collector v1.0")
sleep(0.5)
print("by ssl2k")
sleep(0.5)
print("\nCollecting coins",end="")
driver.get(coinURL)
sleep(3)

driver.find_element_by_xpath(coin).click()
sleep(3)
if (driver.current_url == loginURL):
    driver.find_element_by_xpath(usr).send_keys(usrn)
    driver.find_element_by_xpath(psw).send_keys(pswd)
    driver.find_element_by_xpath(login).click()
    sleep(3)
    driver.find_element_by_xpath(coin).click()

for x in range(3):
    print(".", end="")
    sleep(0.5)
print("\nTotal coins as of now:", driver.find_element_by_xpath(total).text)
amt = driver.find_element_by_xpath(amount)
amt = int(amt.text[26])
if (amt == 1):
    amt = 7
else:
    amt = amt - 1


print(amt, "Coins collected. Exiting...")
sleep(3)
driver.quit()
