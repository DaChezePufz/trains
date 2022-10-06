import requests
import apiKeys
import os

os.system("cls")
if apiKeys.station == "":
	station = input("Enter station code:  ")
	
else: 
	station = apiKeys.station
	print("Station is: "+station)
	

url = "https://transportapi.com/v3/uk/train/station/"+station+"///timetable.json?app_id="+apiKeys.appID+"&app_key="+apiKeys.apiKey+"&train_status=passenger"

#print(url)

print("Getting data from web...")
response = requests.get(url)
rawText = response.text

#print(response.status_code)

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
type, platform = sortedObject[3].split('":"')
arrtype, arrive = sortedObject[7].split('":"')
leavtype, leave = sortedObject[6].split('":"')
desttype, dest = sortedObject[10].split('":"')

# Train 2
sortedObject1 = sortObject(sortedRaw[5])
type1, platform1 = sortedObject1[3].split('":"')
arrtype1, arrive1 = sortedObject1[7].split('":"')
leavtype1, leave1 = sortedObject1[6].split('":"')
desttype1, dest1 = sortedObject1[10].split('":"')

# Train 3
sortedObject2 = sortObject(sortedRaw[7])
type1, platform2 = sortedObject2[3].split('":"')
arrtype1, arrive2 = sortedObject2[7].split('":"')
leavtype1, leave2 = sortedObject2[6].split('":"')
desttype1, dest2 = sortedObject2[10].split('":"')

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