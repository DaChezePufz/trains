## imports
import requests     # importing 'requests'
import apiKeys      # importing 'apiKeys.py'    [LOCAL] [TEMP]
import os           # importing 'os'
import grt          # importing 'grt.py'        [LOCAL]
import stations     # importing 'stations.py'   [LOCAL]
import datetime     # importing 'datettime'
import math         # importing 'math'
import sys          # importing 'sys'
import datetime     # importing 'datetime'
import os.path      # importing 'os.path'
from os import mkdir    # importing 'mkdir' from 'os'


## clearing the shell output
os.system("cls")

## setting some variables
debug = False   # debug to False for normal opperation
reusedRequest = ""  # reusedRequest to blank
resusingRequset = False # reusingRequest to False
numSpacesSixthRow = 0
response = ""


## defining debugMode, params:
## paramToPrint, paramName
def debugMode(paramToPrint, paramName):
    global filePath # defining teh filePath var as global
    
    if debug == True:
        result = f"[\"{paramName}\", \"{paramToPrint}\"]"   # defining the print statment under the results var
        print(result)   # printing the result
        debugLog = open(filePath, "a")  # opening the debug log
        debugLog.write(result+"\n") # writing to the debug log
        debugLog.close()    # closing the debug log

def debugRequest(request, yes):
    global now  # defining the now var as global
    global requestPath  # defining the requestPath var as global

    if yes == True and debug == True:   # will only execute if debug mode is on
        requestFileName = f"request_{now}.json" # making the file path for the request
        requestFilePath = os.path.join(requestPath, requestFileName)    # making the file path for the request
        
        try:    # try statement to allow for file not existing
            requestFile = open(requestFilePath, "a")    #opening the request file
        
            for item in request:
                requestFile.write("%s" % request)   # writing the request to the request file
            requestFile.close() # closing the request file
        
        except:
            requestFile = open(requestFilePath, "x")
            requestFile.close()


if len(sys.argv) == 2:                                                  # if the program is run with 2 arguments
    if sys.argv[1] == "--debug":                                        # if the first argument is '--degbug'
        debug = True                                                    # seting the 'debug' variable to True
        print("*** DEBUG MODE ACTIVATED ***")                           # informing the user that debug mode is avtivated
        now = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")  # storing the current time 
        fileName = "log_"+now+".txt"                                    # creating the file name/ path
        filePath = os.path.join("debugLogs", fileName)                  # creating the file name/ path
        requestPath = os.path.join("debugLogs", "requests")             # creating the file path for the request
        try: debugLog = open(filePath, "x")                             # attmpting to create the debugLog file
        except:                                                         # if above fails:
            os.mkdir("debugLogs")                                           # creating the debug log directory
            os.mkdir(requestPath)                                           # creating the requests directory
            debugLog = open(filePath, "x")                                  # creating the debugLog file
        debugLog = open(filePath, "a")                                  # opening the debug log gile
        debugMode(now, "timeNow")                                       # writing the current time to the debugLog
        debugLog.close()                                                # closing the debug log

elif len(sys.argv) == 4:                                                # if the proggram is run with 4 arguments
    if sys.argv[1] == "--debug":                                        #
        debug = True                                                    # i'm not writing all the comments out again, look at the if statment directly above
        print("*** DEBUG MODE ACTIVATED ***")
        now = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        fileName = "log_"+now+".txt"
        filePath = os.path.join("debugLogs", fileName)
        requestPath = os.path.join("debugLogs", "requests")
        try: debugLog = open(filePath, "x")
        except: 
            os.mkdir("debugLogs")
            os.mkdir(requestPath)
            debugLog = open(filePath, "x")
        debugLog = open(filePath, "a")
        debugMode(now, "timeNow")
        debugLog.close()


    if sys.argv[2] == "--r" and sys.argv[1] == "--debug":               # if the 2nd argument is '--r' and in debug mode
        reuseRequest = True                                             # reusing the request set to True
        reuseRequestPath = requestPath                                  # geting the path
        reuseRequestName = sys.argv[3]                                  # getting the file name from the arguments
        reuseRequestFile = os.path.join(reuseRequestPath, reuseRequestName) # joing all for correct path
        reusedRequest = open(reuseRequestFile, "r")                     # opening
        reusedRequestData = reusedRequest.read()                        # reading
        reusedRequest.close()                                           # closing
        resusingRequset = True

def lateTrainMessageBox():          # just allows you to call a windows message box if there is a late train
    path = os.path.join("windowsMessageBoxes", "lateTrain.vbs")
    os.system(path)




if resusingRequset == True:
    print(f"** RESUING REQUEST: \"{reuseRequestName}\" **")
else:
## checking to see that the user has api credentails present
    if apiKeys.apiKey == "":
        print("Please enter an API Key in the \'apiKeys.py\' file.")
        exit()
    if apiKeys.appID == "":
        print("Please enter an app ID in the \'apiKeys.py\' file.")
        exit()

    debugMode(apiKeys.apiKey, "apiKey")
    debugMode(apiKeys.appID, "appID")
    ## checking if default station preset in 'apiKeys.py', if not requesting one from user
    if apiKeys.station == "":
        station = input("Enter station code:  ")
    else: 
        print("")
        station = apiKeys.station

    debugMode(station, "station")

## fixing certain stations that don't have platforms assined to train manually
def grtPlatWorkings(destinationWPunc):
    global platform
    destination = removePunc(destinationWPunc)
    if station == "grt":
        if destination in grt.plat1:
            platform = "1"
        elif destination in grt.plat2:
            platform = "2"
        else:
            platform = "N/A"
        return platform

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

def stationNameFinder():
    ## searching for and displaying the full station code
    for stationName, stationCode in stationsDB.items():
        stationsDB = stations.stationsInDict
        stationUpper = station.upper()
        if stationUpper == stationCode:
            print(f"The station is: {stationName}")
            stationChosen = stationName

def stationNameRetreiver():
    global stationChosen
    id1 = sortedRaw[1]
    id1sort = sortObject(id1)
    stationNameID = id1sort[3]
    stationNameIDremd = desc, value = stationNameID.split('":"')
    stationName = removePunc(value)
    print(stationName)
    stationChosen = stationName

## defining response for for the request statment, otherwise errors


debugMode(resusingRequset, "reusingRequest")

if resusingRequset == True:
    response = reusedRequestData
    debugMode(response, "response")
    sortedRaw = sortRaw(response)
    debugMode(sortedRaw, "sortedRaw")
else:
    url1 = "https://transportapi.com/v3/uk/train/station/"+station.lower()+"/live.json?app_id="+apiKeys.appID+"&app_key="+apiKeys.apiKey
    debugMode(url1, "url")
    try: 
        response = requests.get(url1)
        
    except: 
        print("Error - check your network connection")


    rawText = response.text
    sortedRaw = sortRaw(rawText)

debugMode(response, "response")
debugRequest(sortedRaw, True)

stationNameRetreiver()

print("""
            Modes:
    
        (1)  Depature Boards ** WIP **
        (2)  Pure Comand Line 
""")

displayMode = int(input("Please enter the mode you would like:  "))



## getting the user to specify how many trains they'd like to see
numOfTrainsToDisplay = int(input("Please enter the number of trains you would like displayed (1, 2 or 3):  "))

## the train locations in sortedRaw 
trainDictValue = [3,5,7,9,11]
trainliveValues = [4,6,8,10,12]
      
## a dictionary with all the values from the object in, with IDs for easier referancing
trainObjects = {
    0:"mode",
    1:"service",
    2:"train_uid",
    3:"platform",
    4:"operator",
    5:"operator_name",
    6:"aimed_departure_time",
    7:"aimed_arrival_time",
    8:"aimed_pass_time",
    9:"origin_name",
    10:"destination_name",
    11:"source",
    12:"category",
    13:"service_timetable"
}

## a dictionary with all the values from the live object in, with IDs for easier referacning
trainLiveObjects = {
    0:"id",
    1:"status",
    2:"expected_arrival_time",
    3:"expected_departure_time",
    4:"best_arrival_estimate_mins",
    5:"best_departure_estimate_mins"
}


def trainObj(trainNum, trainObj, liveBool): #defining the trainObj func with perams: trainNum(local), trainObj(local) and liveBool(local) 
##
## Params:
## 1. trainNum = this is the train number, in decimal, starting from 1
## 2. trainObj = the dictReferance value, in decimal, starting from 0, referance the 2 above dicts
## 3. liveBool = this chooses wether the function referances the planed obj, or the live obj
##      for timetable valies = False
##      for live values = True
##
    if liveBool == False: #if the live option is set to false = choosing the diffrent dicts
        sortedObj = sortObject(sortedRaw[trainDictValue[trainNum]]) #getting the total dictionary for the train number
        
        for objID, objDesc in trainObjects.items():
        
            if trainObj == objID:
        
                try: 
                    desc, value = sortedObj[trainObj].split('":"')
        
                except: 
                    value = "null"
        
                return removePunc(value)

    if liveBool == True:
        sortedObjLive = sortObject(sortedRaw[trainliveValues[trainNum]])
        
        for liveObjID, liveObjDesc in trainLiveObjects.items():
        
            if trainObj == liveObjID:
        
                try: 
                    desc, value = sortedObjLive[trainObj].split('":"')
        
                except: 
                    value = "null"
        
                return removePunc(value)


def atOrigin(trainNum):
    if stationChosen == trainObj(trainNum, 9, False):
        
        # at origin
        print(f"{stationChosen.upper()} --> {trainObj(trainNum, 10, False)}")

    else:
        
        print(f"{trainObj(trainNum, 9, False)} --> {stationChosen.upper()} --> {trainObj(trainNum, 10, False)}")

def lateTrain(trainNumL):
    if trainObj(trainNumL, 1, True) == "LATE":
        lateTrainMessageBox()
        print("""
##           ##########   ##########    ##########
##           ##      ##       ##        ##
##           ##      ##       ##        ##
##           ##########       ##        ##########
##           ##      ##       ##        ##
##########   ##      ##       ##        ##########
""")
        
        print(f"""
Platform: {trainObj(trainNumL, 3, False)}
{atOrigin(trainNumL)}

Departure time: {trainObj(trainNumL, 6, False)}
EXPECTED DEPARTURE TIME: {trainObj(trainNumL, 3, True)}
Best Mins Late: {trainObj(trainNumL, 5, True)}

""")

    else:
        
        print(f"""
Platform: {trainObj(trainNumL, 3, False)}
{atOrigin(trainNumL)}

Departure time: {trainObj(trainNumL, 6, False)}      
        
""")

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
        
        try: 
            platformWithoutPunc = removePunc(platform)
        
        except: 
            platformWithoutPunc = platform
        

        if int(platformWithoutPunc) >= 40:
            spaceIfPlat2Chars = ""
        else:
            spaceIfPlat2Chars = " "

        try: 
            lengthDestination = len(removePunc(dest))
        except: 
            print("")
        
        numSpacesSixthRow = 40 - (lengthDestination + 5 + 2)
        numSpacesSixthRowPrint = " " * int(numSpacesSixthRow)
            
            


        print(f"""
????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
??? {stationNameToDisplay} ???
???                                          ???
???                                  {spaceIfPlat2Chars}Plat {removePunc(platform)} ???
???                                          ???
??? {removePunc(dest)} {numSpacesSixthRowPrint} {removePunc(leave)} ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
???                                          ???
????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

        """)


def commandLineDisplay():
    for i in range (1, numOfTrainsToDisplay+1):
        
        print(f"Train {i}:")
        print("")
        lateTrain(i)


if displayMode == 2:
    commandLineDisplay()

elif displayMode == 1:
    displayBoardsDisplay()


## below are box characters
## ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ???
