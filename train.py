from transportapi_python import Train
from pprint import pprint

# HTTP(S) proxies are supported: https://2.python-requests.org/en/master/user/advanced/#proxies
train = Train(APP_ID="b1f965c3", API_KEY="7d35c36842fcda2da625d900b2c53326")
# Uses the default value station_code: "LBG".
station_code = "grt"
pprint(train.train_timetable())