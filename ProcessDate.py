import datetime
import time
import keyboard
#時間處理函式
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


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            print ("A")
    except:
        break  # if user pressed a key other than the given key the loop will break