from lib2to3.pgen2.token import GREATER
import apiDetails
import requests
import json
from datetime import datetime

parameters = {
    "app_id": "b1f965c3"
    "app_key": "7d35c36842fcda2da625d900b2c53326"
    "station": "grt"
    }


def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

