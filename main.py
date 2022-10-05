import requests

response = requests.get("https://transportapi.com/v3/uk/train/station/adv///timetable.json?app_id=41f6042a&app_key=229f789dd8d9c6d488333521d8960127&train_status=passenger")
rawText = response.text

def sortRaw(message):
    list = message.split("{")
    return list

def sortObject(message):
    list = message.split(",")
    return list

sortedRaw = sortRaw(rawText)
sortedObject = sortObject(sortedRaw[3])

print(sortedObject[7])
print(sortedObject[6])
