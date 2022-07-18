import requests

class DataManager:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/d13dfd3fd2d20f3562411f140fa3ab6b/flightDeals/prices"
        self.auth = {
            "authorization" : "Bearer rodmar"
        }

    def get_data_from_sheet(self):
        print("Retrieving info from Google Sheet...")
        response = requests.get(url=self.sheety_endpoint, headers=self.auth)
        print(response)
        return response