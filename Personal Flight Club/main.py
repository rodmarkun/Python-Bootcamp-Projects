#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data_man = DataManager()
print(data_man.get_data_from_sheet().text)