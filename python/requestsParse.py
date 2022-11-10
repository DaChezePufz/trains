from datetime import datetime
import os.path
from os import mkdir
import sys

def sortRaw(message):
    list = message.split("{")
    return list

def sortObject(message):
    list = message.split(",")
    return list

def removePunc(message):
    finalised = []

    for char in message:
        if(char != '"'):
            finalised.append(char)
    return "".join(finalised)


requestPath = os.path.join("debugLogs", "requests", sys.argv[1])

reusedRequest = open(requestPath, "r")
requestData = reusedRequest.read()

if requestData != "":
    print("Data read succesful.")

sortedRaw = sortRaw(requestData)
print(type(sortedRaw))
count = 0
trainDictValue = 3

values = {
    "London Waterloo": 1
}

sortedObj = sortObject(sortedRaw[0])
for item in sortedObj:
    numTimes = 1
    try: desc, value = sortedObj[count].split('":"')
    except: desc = ""
    #print(desc)
    if removePunc(desc) == sys.argv[2]:
        print(removePunc(value))
    count = count + 1

    if values.hasKey(removePunc(value)):
        #in dict#
        ## read value of numTimes currently in dictionary, and append the numTimes with +1
        for dictItems in values:
            if dictItems.value == removePunc(value):
                values[value].append(value+1)


        print("")
    else:
        #not in dict#
        addList = [value, numTimes]
        ## append add list to  `values` dict 



