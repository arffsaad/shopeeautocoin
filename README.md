## SHOPEE AUTO COIN COLLECTION V2.0

> due to my bad motivation (and my new job) I havent maintained this repo a lot. Will find the time to amp up the whole thing soon. If you want to use it, I would recommend to Fork and fix anything broken, and PR. (ill review and see if its good to merge)

### to-do
- detect contingencies in login (QR scan, no 2FA etc)


Autocollect Shopee Coins everyday, without fail. The script will login, and collect your coins for you. It is built with persistency, which means you only need to authorize 2FA only once, and it will flawlessly work every time.

### Pre-requisites
- Python 3.8 or greater (tested on 3.10, but playwright should work fine at 3.8)
- `pip install pytest-playwright`
- `playwright install`

### Usage
- Clone Repository
- Run autocoin.py, it will launch the first login routine. Follow the prompts to authorize 2FA, and store your session persistently.
- After completing the steps, schedule the script to run once every day.
  - Windows
    - Open Task scheduler, and create new task.
    - Execute a program > set path as path to python executable.
    - set parameters as path to autocoin.py
    - Set frequency as repeat daily, select a time where your PC/Laptop will be running.
  - Linux/MacOS
    - add an entry in crontab with `crontab -e`
    - `0 8 * * * /path/to/python3 /path/to/autocoin.py # example, will run the script at 8AM every day`
