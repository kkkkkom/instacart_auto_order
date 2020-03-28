
### import
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import test_email
from datetime import datetime
import pdb
import sys

from login import *
from poll_target_dates import *
from place_order import *

def auto_order(login_email='', login_password='', target_dates='', card_number='', card_exp='', card_cvc=''):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver = login(driver, login_email, login_password)
    driver, t = poll_target_dates(driver, target_dates)
    driver = place_order(driver, t, card_number, card_exp, card_cvc)
    
    return

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Parse args for auto place order on instacart')
    parser.add_argument('-login_email', type=str, help='email account for instacart')
    parser.add_argument('-login_password', type=str, help='password for instacart account')
    parser.add_argument('-target_dates', type=str, help='target dates for order, from low to high priority') # -target_dates "Apr 4,Apr 3"
    parser.add_argument('-card_number', type=str, help='credit card number for payment')
    parser.add_argument('-card_exp', type=str, help='credit card expiration date')
    parser.add_argument('-card_cvc', type=str, help='CVC number for the credit card')
    args = parser.parse_args()

    auto_order(args['login_email'],args['login_password'],args['target_dates'],args['card_number'],args['card_exp'],args['card_cvc'])
