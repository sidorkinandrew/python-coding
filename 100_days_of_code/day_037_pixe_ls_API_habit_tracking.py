from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "andriy"

TOKEN = "*************************************************************************************************************"

GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Read Page",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages have you read today?"),
}

# POST
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
