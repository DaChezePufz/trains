from lib2to3.pgen2.token import GREATER
import apiDetails
import requests
import json
from datetime import datetime
class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        # self.get_data(api)

        parameters = {
#            "username": ""
            
        }
        self.get_user_data(api, parameters)

if __name__ == "__main__":
    __init__()

station_code = "grt"
date = ""
time = ""


api_call = MakeApiCall("https://transportapi.com/v3/uk/train/station/bsk///timetable.json?app_id=b1f965c3&app_key=7d35c36842fcda2da625d900b2c53326&train_status=passsenger")

