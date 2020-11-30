import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import keyboard

#FB文章抓取練習

load_dotenv()
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")

sel_email = chrome.find_element_by_id("email")
sel_password = chrome.find_element_by_id("pass")


sel_email.send_keys(os.getenv('EMAIL'))
sel_password.send_keys(os.getenv('PASSWORD'))

time.sleep(1)

sel_password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/'+os.getenv('ACCOUNT'))

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')
contents = soup.find_all('div', {'class': 'pybr56ya dati1w0a hv4rvrfc n851cfcs btwxx1t3 j83agx80 ll8tlv6m'})

for content in contents:
    print(content.find_all('div', {'class': 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'}).getText())
    
chrome.close()
