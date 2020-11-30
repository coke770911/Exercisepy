from selenium import webdriver
import time
import keyboard

options = webdriver.ChromeOptions()
#背景執行
#options.add_argument('--headless')
#指定瀏覽器解析度 
#options.add_argument('window-size=1920x1000')
#啟動就最大化
options.add_argument('--start-maximized')
#不加載圖片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false') 
#以最高權限運行
options.add_argument('--no-sandbox')
#加上這個屬性來規避bug
options.add_argument('--disable-gpu')

while True:  
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            #放入要重複執行的程式碼    
            chrome = webdriver.Chrome(chrome_options=options)
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
            time.sleep(1)
            chrome.switch_to_alert().accept()
            time.sleep(1)
            #關閉分頁
            #chrome.close()
            #關閉瀏覽器
            chrome.quit()            
    except:
        break  # if user pressed a key other than the given key the loop will break

