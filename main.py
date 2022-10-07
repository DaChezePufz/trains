## imports
import requests
import apiKeys
import os
import grt # 'grt.py'
import csv

## clearing the shell output
os.system("cls")

with open('stationsForm.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('stations_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        stationsCode = {rows[0]:rows[1] for rows in reader}


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
	#print("Station is: "+station)

stationUpper = station.upper()

for stationName, stationCode in stationsCode.items():
    if stationUpper == stationCode:
        print(f"The station is: {stationName}")

## fixing certain stations that don't have platforms assined to train manually
def grtPlatWorkings(destinationWPunc):
    #print(destinationWPunc)
    destination = removePunc(destinationWPunc)
    #print(destination)
    if station == "grt":
        if destination in grt.plat1:
            platform = "1"
            #print("set plat 1")

        elif destination in grt.plat2:
            platform = "2"
            #print("set plat 2")

        else:
            platform = "N/A"
            #print("set plat n/a")
        return platform

## making the url for the api call
url1 = "https://transportapi.com/v3/uk/train/station/"+station+"///timetable.json?app_id="+apiKeys.appID+"&app_key="+apiKeys.apiKey+"&train_status=passenger"
url2 = "https://transportapi.com/v3/uk/train/station/"+station+"///timetable.json?app_id="+apiKeys.appID1+"&app_key="+apiKeys.apiKey1+"&train_status=passenger"
url3 = "https://transportapi.com/v3/uk/train/station/"+station+"///timetable.json?app_id="+apiKeys.appID2+"&app_key="+apiKeys.apiKey2+"&train_status=passenger"

## defining response for stuff
response = ""
credsSet = 1

## getting the data from the api
print("Attempting to verify credentials...")

try: response = requests.get(url1)
except:
    if response.statuscode == "403":
        credsSet = credsSet + 1

        try: response = requests.get(url2)
        except:
            if response.statuscode == "403":
                credsSet = credsSet + 1

                try: response = requests.get(url3)
                except:
                    if response.statuscode == "403":
                        print("All 3 sets of credentials are invalid, enter valid ones.")
                        exit()

#print(credsSet)

rawText = response.text

#print(response.status_code)

## some formatting
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

# Train 1
sortedObject = sortObject(sortedRaw[3])
#print(sortedObject)
try: desttype, dest = sortedObject[10].split('":"')
except: dest = "N/A"
try: type, platform = sortedObject[3].split('":"')
except: platform = grtPlatWorkings(dest)
try: arrtype, arrive = sortedObject[7].split('":"')
except: arrive = "N/A"
leavtype, leave = sortedObject[6].split('":"')


# Train 2
sortedObject1 = sortObject(sortedRaw[5])
#print(sortedObject1)
desttype1, dest1 = sortedObject1[10].split('":"')
try: type1, platform1 = sortedObject1[3].split('":"')
except: platform1 = grtPlatWorkings(dest1)
try: arrtype1, arrive1 = sortedObject1[7].split('":"')
except: arrive1 = "N/A"
leavtype1, leave1 = sortedObject1[6].split('":"')


# Train 3
sortedObject2 = sortObject(sortedRaw[7])
#print(sortedObject2)
desttype2, dest2 = sortedObject2[10].split('":"')
try: type2, platform2 = sortedObject2[3].split('":"')
except: platform2 = grtPlatWorkings(dest2)
try: arrtype2, arrive2 = sortedObject2[7].split('":"')
except: arrive2 = "N/A"
leavtype2, leave2 = sortedObject2[6].split('":"')


print(f"""

Train 1:

Platform: {removePunc(platform)}
Arriving at station @ {removePunc(arrive)}
Leaving station @ {removePunc(leave)}
Destination: {removePunc(dest)}

Train 2:

Platform: {removePunc(platform1)}
Arriving at station @ {removePunc(arrive1)}
Leaving station @ {removePunc(leave1)}
Destination: {removePunc(dest1)}

Train 3:

Platform: {removePunc(platform2)}
Arriving at station @ {removePunc(arrive2)}
Leaving station @ {removePunc(leave2)}
Destination: {removePunc(dest2)}

""")