
def ObjToSortedArray(data):

    def GetSortArgumet (item):
        return(item['date'])

    AllHomeWork = []

    for i in data:
        for j in data[i]:
            AllHomeWork.append({'subj':i,'hometask':j["task"],'date':j["deadline"]})

    AllHomeWork.sort( key = GetSortArgumet)

    return AllHomeWork

# obj = {"Math":[{'task':'asd','deadline':"10"},{'task':'fgh','deadline':"4"},{'task':'jkl','deadline':"2"}],"Dm":[{'task':'qwe','deadline':"6"},
# {'task':'rty','deadline':"5"},{'task':'uio','deadline':"9"}]}
#
#
# for i in obj:
#     print(obj[i])
#
# print("____________________")
#
# arr = ObjToSortedArray(obj)
#
# for i in arr:
#     print(i)
