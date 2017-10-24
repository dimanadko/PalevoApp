import datetime
import json

def NextClassIs(subj):
    today = datetime.date.today()
    weekday = datetime.date.weekday(today)

    TimeTableFile = open("Timetable.json",'r')
    TimeTable = json.load(TimeTableFile)
    TimeTableFile.close()

    i = 0
    interval = 0
    breaker = False
    while True:
        k = i+weekday
        if k>6:
            k=k-7
        for j in TimeTable[k]:
            if (subj == j):
                interval = i
                breaker = True
        i = i+1
        if breaker:
            break



    todayClass = datetime.date.today()
    d = datetime.timedelta(days = +interval)
    nextClass = todayClass + d
    # print (nextClass)
    return (nextClass)
