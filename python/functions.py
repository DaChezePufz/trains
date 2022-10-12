import datetime
import afterDateNds
import apiKeys
import stations
import grt

station = ""


def getAndDisplayTime():
    now = datetime.datetime.now()   
    prefixDateList = afterDateNds.afterDatePrefix
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

def apiCredsCheck():
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