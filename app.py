from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import datetime
import time

def main():
    StartDate = time.strptime("2021/1/1", "%Y/%m/%d")
    EndDate = time.strptime("2021/7/1", "%Y/%m/%d")
    StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
    EndDate =  datetime.date(EndDate[0], EndDate[1], EndDate[2])
    RangeDate = datetime.timedelta(days = 7)


    while StartDate <= EndDate:
        print (StartDate)
        print (StartDate + RangeDate)
        print ("_______________")
        StartDate = StartDate + RangeDate

main()