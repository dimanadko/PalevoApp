import json

TimeTable = [
    [
        "Programming"
    ],
    [
        "Matan"
    ],
    [
        "Histoty"
    ],
    [
        "Matan Lection","OS","LAAG","English1"
    ],
    [
        "Matan Lection","Dm"
    ],
    [

    ],
    [

    ]
]

TableFile = open("Timetable.json","w")
json.dump(TimeTable,TableFile)
TableFile.close()
print(TimeTable)
