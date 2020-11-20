from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('chromedriver', chrome_options=options)
chrome.get("https://www.citibank.com.tw/sim/zh-tw/credit-cards/epp-form.htm")

cardnumber = chrome.find_element_by_id("cardnumber")
annual_above = chrome.find_element_by_id("annual_above")
ID = chrome.find_element_by_id("ID")
check = chrome.find_element_by_xpath("//input[@value='202011elife2000']")
submit = chrome.find_element_by_class_name('submit')

annual_above.click()
cardnumber.send_keys("1234")
ID.send_keys("123456789")
check.click()
submit.click()

chrome.switch_to_alert().accept() 