import json
import Obj_to_sorted_Array
data = json.load(open("Data.json","r"))

arraydata = Obj_to_sorted_Array.ObjToSortedArray(data)
for i in arraydata:
    print(i)
