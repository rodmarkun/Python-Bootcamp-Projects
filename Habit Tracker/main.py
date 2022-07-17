import requests
from datetime import datetime

USERNAME = "rodmarkun"
TOKEN = "aaud2907313kadpaw1214124"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# Create User
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "readinggraph",
    "name" : "Reading Graph",
    "unit" : "Pages",
    "type" : "int",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# Create a Graph
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/readinggraph"

pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "50"
}

#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)