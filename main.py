import requests
from datetime import datetime
TOKEN = 'wowdavidsu'
USERNAME = 'davidsu'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
GRAPHID = 'davidgraphid'
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params = {
    'id':GRAPHID,
    'name':'Coding Streak',
    'unit':'Hours',
    'type':'float',
    'color':'ajisai'
}

headers = {
    'X-USER-TOKEN':TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph_edit = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

today = datetime.now()

graph_edit_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity':'4',
}

# response = requests.post(url=graph_edit, json = graph_edit_params, headers = headers)

# print(response.text)
graph_change = {
    'quantity':'6',
}
response = requests.put(url = graph_edit+f'/{graph_edit_params["date"]}', json= graph_change, headers = headers)

print(response.text)