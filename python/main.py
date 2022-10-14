## imports
import requests     # importing 'requests'
import apiKeys      # importing 'apiKeys.py'    [LOCAL] [TEMP]
import os           # importing 'os'
import grt          # importing 'grt.py'        [LOCAL]
import stations     # importing 'stations.py'   [LOCAL]
import datetime     # importing 'datettime'
import math         # importing 'math'
import functions    # importing 'functions.py'  [LOCAL]

## clearing the shell output
os.system("cls")



## defining the database as a local variable


platform = 0
numSpacesSixthRow = 0



## making 2nd station code var with uppercase
print("emily williams")

print("emily williams")
print("emily williams")


## making the url for the api call
url1 = "https://transportapi.com/v3/uk/train/station/"+functions.station.lower()+"///timetable.json?app_id="+apiKeys.appID+"&app_key="+apiKeys.apiKey+"&train_status=passenger"

## defining response for for the request statment, otherwise errors
response = ""

try: response = requests.get(url1)
except: print("Error - check your network connection")
rawText = response.text



sortedRaw = functions.sortRaw(rawText)
print("emily williams")
print("""
            Modes:
    
        (1)  Depature Boards
        (1.5) emily williams
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
        sortedObject = functions.sortObject(sortedRaw[trainDictValue[i]])

        try: desttype, dest = sortedObject[10].split('":"')
        except: dest = "N/A"
        try: type, platform = sortedObject[3].split('":"')
        except: platform = functions.grtPlatWorkings(dest)
        try: arrtype, arrive = sortedObject[7].split('":"')
        except: arrive = "N/A"
        try: leavtype, leave = sortedObject[6].split('":"')
        except: leave = "N/A"

except: print("")        
        

def commandLineDisplay():
    print("emily williams")
    print("emily williams")
    try:
        print(f"""

Train {i}:
Platform: {functions.removePunc(platform)}
Arriving at station @ {functions.removePunc(arrive)}
Leaving station @ {functions.removePunc(leave)}
Destination: {functions.removePunc(dest)}
Emily Williams
        """)
    except: print("")
    os.system("pause")


frontSpaces = ""
backSpaces = ""

def displayBoardsDisplay():
    print("")
    # 40 wide, 1 space either side for padding then box characters
    if numOfTrainsToDisplay == 1:
        lengthStationName = len(functions.stationChosen)
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

            stationNameToDisplay = frontSpaces+functions.stationChosen+backSpaces
        else:
            cutStationName = functions.stationChosen[:40]
            stationNameToDisplay = cutStationName
        try: platformWithoutPunc = functions.removePunc(platform)
        except: platformWithoutPunc = platform
        if int(platformWithoutPunc) >= 40:
            spaceIfPlat2Chars = ""

        else:
            spaceIfPlat2Chars = " "

        lengthDestination = len(functions.removePunc(dest))

        numSpacesSixthRow = 40 - (lengthDestination + 5 + 2)
        numSpacesSixthRowPrint = " " * int(numSpacesSixthRow)
            
            


        print(f"""
┌──────────────────────────────────────────┐
│ {stationNameToDisplay} │
│                                          │
│                                  {spaceIfPlat2Chars}Plat {functions.removePunc(platform)} │
│                                          │
│ {functions.removePunc(dest)} {numSpacesSixthRowPrint} {functions.removePunc(leave)} │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
│                                          │
└──────────────────────────────────────────┘

        """)


if displayMode == 2:
    commandLineDisplay()

elif displayMode == 1:
    displayBoardsDisplay()


##
## ┌ ┐ └ ┘ ├ ┤ ┬ ─ │ ┴ ┼ ╱ ╲
