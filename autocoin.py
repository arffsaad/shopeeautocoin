#!/bin/bash python3

from playwright.sync_api import sync_playwright
from time import sleep as sl
import os

# persistence, load an existing user data dir.
#user_data_dir = 'udd' #testing
user_data_dir = 'persistence' #production

print("""
    _   _   _ _____ ___   ____ ___ ___ _   _ 
   / \ | | | |_   _/ _ \ / ___/ _ \_ _| \ | |
  / _ \| | | | | || | | | |  | | | | ||  \| |
 / ___ \ |_| | | || |_| | |__| |_| | || |\  |
/_/   \_\___/  |_| \___/ \____\___/___|_| \_|
""")
print("========== Shopee Coin AutoCollector v2.0 ==========\n\n")
sl(1)
print("Checking credentials.txt...")
sl(1)
# check if file exists
if not(os.path.isfile('credentials.txt')):
    print("Credentials.txt does not exist. First login detected. Please follow prompts to login and authorize 2FA")
    sl(1)
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(user_data_dir, headless=True)
        # get current page
        page = browser.pages[0]
        page.goto('https://shopee.com.my/buyer/login?next=https%3A%2F%2Fshopee.com.my%2Fshopee-coins', wait_until = 'domcontentloaded')
        page.reload()
        # do login
        try:
            page.locator('xpath=//button[contains(text(), "English")]').click()
        except:
            nothing = 0
        username = input("Enter Username(Or phone number): ")
        password = input("Enter Password: ")
        print("Logging in...")
        sl(1)
        page.locator('input[name="loginKey"]').fill(username)
        page.locator('input[name="password"]').fill(password)
        # press enter
        page.keyboard.press('Enter')
        print("Performing 2FA Authorization. Please check your Whatsapp, and click the link to authorize.\n")
        sl(1)
        page.locator('xpath=//div[contains(text(), "Authentication Link")]').click()
        page.locator('xpath=//button[contains(text(), "OK")]').click()
        input("Press Enter once you have authorized the login.")
        page.goto('https://shopee.com.my')
        # get text from navbar__username
        print('Logged in as:', page.locator("#stardust-popover1 > div > div > div.navbar__username").inner_text())
        print("Saving Credentials...")
        with open('credentials.txt', 'w') as f:
            f.write(username + '\n')
            f.write(password)
        sl(3)
        input("First login succesful!\nCredentials saved in credentials.txt.\nPlease create a Scheduled Task (Windows) or Cron Job (Linux) to run this script every 24 hours.\nScript has finished.\n\nPress Enter to continue...")
        browser.close()


else:
    print("Credentials.txt found. Collecting coins...")
    # get credentials
    with open('credentials.txt', 'r') as f:
        credentials = f.read().splitlines()
        username = credentials[0]
        password = credentials[1]
        print("Credentials loaded.")
    # do normal routine
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(user_data_dir, headless=True)
            # get current page
            page = browser.pages[0]
            page.goto('https://shopee.com.my/buyer/login?next=https%3A%2F%2Fshopee.com.my%2Fshopee-coins', wait_until = 'domcontentloaded')
            sl(2)
            page.reload()
            print("Checking if logged in...")
            if (page.url == 'https://shopee.com.my/buyer/login?next=https%3A%2F%2Fshopee.com.my%2Fshopee-coins'):
                # do login
                print("Not logged in. Logging in...")
                page.locator('input[name="loginKey"]').fill(username)
                page.locator('input[name="password"]').fill(password)
                # press enter
                page.keyboard.press('Enter')
            else:
                # wait for dom, click get coin.
                print("Logged in. Collecting...")
            # click on xpath
            try:
                page.locator('xpath=//button[contains(text(), "Check in today")]').click()
            except:
                try:
                    page.locator('xpath=//button[contains(text(), "Come back tomorrow")]').click()
                    print("Coins already collected today.")
                except:
                    print("Unknown Exception.")
            sl(2)
            page.goto("https://shopee.com.my/user/coin/list")
            coinbal = page.locator("#main > div > div.dYFPlI > div > div.xMDeox > div > div > div.NpdN3L > div.ZBdeXm").inner_text()
            cointoday = page.locator("#main > div > div.dYFPlI > div > div.xMDeox > div > div > div:nth-child(2) > div.rXcU7s > div:nth-child(1) > div > div.R519Sm._5Q-g4s").inner_text()
            print("\nCoins Collected!\nCoins balance: ", coinbal, "\nCoins Collected Today: ", cointoday, "\n\n")
            browser.close()
