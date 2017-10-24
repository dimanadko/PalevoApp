import json
import datetime
import DeadlineCounter
import sys


def ApendHomeWork (subj,task,deadline):
    data_read = open("Data.json",'r')
    TasksToDo = json.load(data_read)
    data_read.close()

    breaker = True
    for i in TasksToDo:
        if subj == i:
            breaker = False

    if breaker:
        sys.exit("No Such Subject Exist")

    if (deadline == ''):
        deadline = str(DeadlineCounter.NextClassIs(subj))

    data_write = open("Data.json",'w')
    TasksToDo[subj].append({"task":task,"deadline":deadline})
    json.dump(TasksToDo,data_write)
    data_write.close()

    print(subj,TasksToDo[subj])

Subject = input('Enter your subject: ')
Homework = input('Enter new homework: ')
TimeToDo = input("Enter deadline: ")


ApendHomeWork(Subject,Homework,TimeToDo)
