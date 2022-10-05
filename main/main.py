from email import message
import requests

response = requests.get("https://transportapi.com/v3/uk/train/station/adv///timetable.json?app_id=b1f965c3&app_key=7d35c36842fcda2da625d900b2c53326&train_status=passenger")

rawText = response.text

list = rawText.split("{")

test = list[3]

information = test.split(",")

print(information[6])