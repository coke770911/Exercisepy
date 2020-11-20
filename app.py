from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import keyboard

options = Options()
options.add_argument("--disable-notifications")

while True:  
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
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
            chrome.close()
            time.sleep(5)
    except:
        break  # if user pressed a key other than the given key the loop will break

print("stop")