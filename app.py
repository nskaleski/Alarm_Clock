import datetime

alarmHour = int(input("what time do you want to wake up? "))

alarmMinute = int(input("what minute do you want to wake up at? "))

amPm = str(input("am or pm: "))

if(amPm == "pm"):
    alarmHour = alarmHour + 12

while(True):
    if(alarmHour == datetime.datetime.now().hour and
       alarmMinute == datetime.datetime.now().minute):
        print("WAKE UP!")
        break

print("exited")