import requests
import time

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]

    location = (latitude, longitude)

    print(f"Seconds since the Epoch: {time.time()}s\nISS current location (lat, long): {location}\n")
    time.sleep(1)