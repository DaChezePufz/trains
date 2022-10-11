## imports
from email import message
from tkinter import N
from turtle import back
import requests     # importing 'requests'
import apiKeys      # importing 'apiKeys.py'    [LOCAL] [TEMP]
import os           # importing 'os'
import grt          # importing 'grt.py'        [LOCAL]
import stations     # importing 'stations.py'   [LOCAL]
import datetime     # importing 'datettime'
import afterDateNds # importing 'afterDateNds   [LOCAL]
import math         # importing 'math'

## clearing the shell output
os.system("cls")

## converting the foreighn dictionary to local
prefixDateList = afterDateNds.afterDatePrefix

## getting the date and time at which the query was placed
now = datetime.datetime.now()

## getting all the time values as their own seperate variables
currentWeekDay = now.strftime("%A")
currentMonth = now.strftime("%B")
currentYear = now.strftime("%Y")
currentMonthDay = now.strftime("%d")

for dayOfMonth, dayOfMonthSuffix in prefixDateList.items():
    if dayOfMonth == currentMonthDay:
        monthDayPrefix = dayOfMonthSuffix

currentHour = now.strftime("%H")
currentMinute = now.strftime("%M")
currentSecond = now.strftime("%S")

print(currentWeekDay,currentMonthDay+monthDayPrefix,currentMonth,currentYear+" - "+currentHour+":"+currentMinute+":"+currentSecond)

## defining the database as a local variable
stationsDB = stations.stationsInDict

platform = 0
numSpacesSixthRow = 0

## checking to see that the user has api credentails present
if apiKeys.apiKey == "":
    print("Please enter an API Key in the \'apiKeys.py\' file.")
    exit()
if apiKeys.appID == "":
    print("Please enter an app ID in the \'apiKeys.py\' file.")
    exit()

## checking if default station preset in 'apiKeys.py', if not requesting one from user
if apiKeys.station == "":
	station = input("Enter station code:  ")
else: 
	station = apiKeys.station

## making 2nd station code var with uppercase
stationUpper = station.upper()

## searching for and displaying the full station code
for stationName, stationCode in stationsDB.items():
    if stationUpper == stationCode:
        print(f"The station is: {stationName}")
        stationChosen = stationName

## fixing certain stations that don't have platforms assined to train manually
def grtPlatWorkings(destinationWPunc):
    destination = removePunc(destinationWPunc)
    if station == "grt":
        if destination in grt.plat1:
            platform = "1"
        elif destination in grt.plat2:
            platform = "2"
        else:
            platform = "N/A"
        return platform

## making the url for the api call
url1 = "https://transportapi.com/v3/uk/train/station/"+station+"///timetable.json?app_id="+apiKeys.appID+"&app_key="+apiKeys.apiKey+"&train_status=passenger"

## defining response for for the request statment, otherwise errors
response = ""

try: response = requests.get(url1)
except: print("Error - check your network connection")
rawText = response.text

## some formatting and json parsing
def removePunc(message):
    finalised = []

    for char in message:
        if(char != '"'):
            finalised.append(char)
    return "".join(finalised)

def sortRaw(message):
    list = message.split("{")
    return list

def sortObject(message):
    list = message.split(",")
    return list

sortedRaw = sortRaw(rawText)

print("""
            Modes:
    
        (1)  Depature Boards
        (2)  Pure Comand Line
""")

displayMode = int(input("Please enter the mode you would like:  "))



## getting the user to specify how many trains they'd like to see
numOfTrainsToDisplay = int(input("Please enter the number of trains you would like displayed (1, 2 or 3):  "))

## the train locations in sortedRaw 
trainDictValue = [3,5,7,9,11]

## 'try' statement means that the program will not error out if less than the number of trains 
## asked for are not available, or if the program cannot parse a certain line due to there not 
## being a colon as the value is 'null' like some platforms on minor stations, or arrival times 
## if the train starts from that location (and other similar situations)
try: 
    for i in range(1, (numOfTrainsToDisplay+1)):
        sortedObject = sortObject(sortedRaw[trainDictValue[i]])

        try: desttype, dest = sortedObject[10].split('":"')
        except: dest = "N/A"
        try: type, platform = sortedObject[3].split('":"')
        except: platform = grtPlatWorkings(dest)
        try: arrtype, arrive = sortedObject[7].split('":"')
        except: arrive = "N/A"
        try: leavtype, leave = sortedObject[6].split('":"')
        except: leave = "N/A"

except: print("")        
        

def commandLineDisplay():
    try:
        print(f"""

Train {i}:
Platform: {removePunc(platform)}
Arriving at station @ {removePunc(arrive)}
Leaving station @ {removePunc(leave)}
Destination: {removePunc(dest)}
        """)
    except: print("")
    os.system("pause")


frontSpaces = ""
backSpaces = ""

def displayBoardsDisplay():
    print("")
    # 40 wide, 1 space either side for padding then box characters
    if numOfTrainsToDisplay == 1:
        lengthStationName = len(stationChosen)
        numOfSpacesToPrint = 40 - lengthStationName

        if numOfSpacesToPrint >= 1:
            
            if (numOfSpacesToPrint % 2) == 0:       #even
                halfNumSpaces = numOfSpacesToPrint / 2
                frontNumSpaces = halfNumSpaces
                backNumSpaces = halfNumSpaces
                print()
                frontSpaces = " " * int(frontNumSpaces)
                backSpaces = " " * int(backNumSpaces)

            else:
                numOfSpacesToPrint = numOfSpacesToPrint + 1
                halfNumSpaces = numOfSpacesToPrint / 2
                frontNumSpaces = halfNumSpaces
                backNumSpaces = halfNumSpaces - 1
                frontSpaces = " " * int(frontNumSpaces)
                backSpaces = " " * int(backNumSpaces)

            stationNameToDisplay = frontSpaces+stationChosen+backSpaces
        else:
            cutStationName = stationChosen[:40]
            stationNameToDisplay = cutStationName
        try: platformWithoutPunc = removePunc(platform)
        except: platformWithoutPunc = platform
        if int(platformWithoutPunc) >= 40:
            spaceIfPlat2Chars = ""
        else:
            spaceIfPlat2Chars = " "

        lengthDestination = len(removePunc(dest))

        numSpacesSixthRow = 40 - (lengthDestination + 5 + 2)
        numSpacesSixthRowPrint = " " * int(numSpacesSixthRow)

        print(f"""
┌──────────────────────────────────────────┐
│ {stationNameToDisplay} │
│                                          │
│                                  {spaceIfPlat2Chars}Plat {removePunc(platform)} │
│                                          │
│ {removePunc(dest)} {numSpacesSixthRowPrint} {removePunc(leave)} │
│


        """)


if displayMode == 2:
    commandLineDisplay()

elif displayMode == 1:
    displayBoardsDisplay()


##
## ┌ ┐ └ ┘ ├ ┤ ┬ ─ │ ┴ ┼ ╱ ╲